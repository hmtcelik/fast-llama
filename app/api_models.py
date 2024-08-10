from pydantic import BaseModel


class HealthCheck(BaseModel):
    healthy: bool


class QuestionRequest(BaseModel):
    q: str


class QuestionResponse(BaseModel):
    answer: str
