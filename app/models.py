from pydantic import BaseModel
from typing import Optional

class LLMRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = 100
    temperature: Optional[float] = 0.7
    stream: Optional[bool] = False

class LLMResponse(BaseModel):
    text: str
    tokens_used: int
    model_version: str 