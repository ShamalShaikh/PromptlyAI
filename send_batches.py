import httpx
import asyncio

async def send_request(client, prompt, max_tokens=50):
    response = await client.post(
        "http://127.0.0.1:8000/generate",
        json={"prompt": prompt, "max_tokens": max_tokens}
    )
    return response.json()

async def send_batch_requests(prompts):
    async with httpx.AsyncClient() as client:
        tasks = [send_request(client, prompt) for prompt in prompts]
        responses = await asyncio.gather(*tasks)
        return responses

def main():
    prompts = [
        "Once upon a time",
        "In a galaxy far, far away",
        "The quick brown fox",
        "To be or not to be",
        "In the beginning"
    ]
    responses = asyncio.run(send_batch_requests(prompts))
    for i, response in enumerate(responses):
        print(f"Response {i+1}: {response}")

if __name__ == "__main__":
    main() 