from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends, Request
from pydantic import BaseModel
import logging
import time
from .services import LLMService, get_llm_service
from .models import LLMRequest, LLMResponse
from .rate_limiter import RateLimiter

# Initialize FastAPI app with metadata
app = FastAPI(
    title="LLM API Service",
    description="Production-ready LLM integration",
    version="1.0.0"
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Middleware for error handling and monitoring
@app.middleware("http")
async def add_monitoring(request: Request, call_next):
    start_time = time.time()
    try:
        response = await call_next(request)
        duration = time.time() - start_time
        status_code = response.status_code
        logger.info(f"Request processed: duration={duration:.2f}s, status={status_code}")
        return response
    except Exception as e:
        logger.error(f"Request failed: {e}")
        raise

# Define the log_request_metrics function
async def log_request_metrics(request: LLMRequest, response: LLMResponse):
    # Implement your logging logic here
    logger.info(f"Request: {request}")
    logger.info(f"Response: {response}")

# API Endpoints
@app.post("/generate", response_model=LLMResponse)
async def generate_text(
    request: LLMRequest,
    background_tasks: BackgroundTasks,
    llm_service: LLMService = Depends(get_llm_service)
):
    try:
        response = await llm_service.generate(request)
        background_tasks.add_task(log_request_metrics, request=request, response=response)
        return response
    except Exception as e:
        logger.error(f"Error generating text: {e}")
        raise HTTPException(status_code=500, detail=str(e))