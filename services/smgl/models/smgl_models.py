from pydantic import BaseModel, field_validator
from datetime import datetime

# Модель для объекта session внутри ответа
class SessionModel(BaseModel):
    id: str
    status: str
    created_at: datetime
    updated_at: datetime

    @field_validator('status')
    def check_status(cls, value):
        valid_statuses = ['created', 'pending', 'completed', 'failed']
        if value not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        return value

# Модель для полного ответа API
class CreateSessionResponseModel(BaseModel):
    status: str
    session: SessionModel

    @field_validator('status')
    def check_response_status(cls, value):
        if value != "ok":
            raise ValueError("Response status must be 'ok'")
        return value


