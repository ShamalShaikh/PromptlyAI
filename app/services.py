import asyncio
import logging
from .models import LLMRequest, LLMResponse
from transformers import pipeline

logger = logging.getLogger(__name__)

class LLMService:
    def __init__(self):
        self.model = self.load_llm_model()
        self._request_queue = asyncio.Queue()
        self._batch_size = 5
        self._processing_task = None

    def load_llm_model(self):
        # Load a pre-trained model from Hugging Face
        return pipeline("text-generation", model="gpt2")

    async def start_processing(self):
        if self._processing_task is None:
            self._processing_task = asyncio.create_task(self._process_queue())

    async def generate(self, request: LLMRequest) -> LLMResponse:
        await self.start_processing()  # Ensure the processing task is started
        future = asyncio.Future()
        await self._request_queue.put((request, future))
        return await future

    async def _process_queue(self):
        while True:
            batch = []
            try:
                while len(batch) < self._batch_size:
                    try:
                        request, future = await asyncio.wait_for(self._request_queue.get(), timeout=0.1)
                        batch.append((request, future))
                    except asyncio.TimeoutError:
                        break

                if batch:
                    responses = await self._process_batch(batch)
                    for (_, future), response in zip(batch, responses):
                        future.set_result(response)

            except Exception as e:
                logger.error(f"Error processing batch: {e}")
                for _, future in batch:
                    if not future.done():
                        future.set_exception(e)

    async def _process_batch(self, batch):
        responses = []
        for request, _ in batch:
            try:
                # Use the model to generate text
                generated = self.model(request.prompt, max_length=request.max_tokens)
                generated_text = generated[0]['generated_text']
                response = LLMResponse(
                    text=generated_text,
                    tokens_used=len(generated_text.split()),
                    model_version="gpt2"
                )
                responses.append(response)
            except Exception as e:
                logger.error(f"Error processing request: {e}")
                responses.append(LLMResponse(text="", tokens_used=0, model_version="gpt2"))
        return responses

def get_llm_service():
    return LLMService() 