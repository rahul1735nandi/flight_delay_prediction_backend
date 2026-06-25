from pydantic import BaseModel

class PredictionResponse(BaseModel):
    is_delayed: bool
    prediction: str
    delay_probability: float