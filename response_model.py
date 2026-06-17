from pydantic import BaseModel

class PredictionResponse(BaseModel):
    is_delayed: int
    prediction: str
    delay_probability: float