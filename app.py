from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from request_model import FlightRequest
from model_loader import model, MODEL_THRESHOLD
from prediction_service import prepare_input_data
from response_model import PredictionResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Flight Delay Prediction API Running"
    }

@app.post("/predict", response_model=PredictionResponse)
def predict(request: FlightRequest):
    input_df = prepare_input_data(
        origin=request.origin,
        dest=request.dest,
        airline=request.airline,
        month=request.month,
        day_of_week=request.day_of_week,
        distance=request.distance,
        crs_dep_time=request.crs_dep_time
    )

    delay_probability = (model.predict_proba(input_df)[0][1])

    is_delayed = (True if delay_probability >= MODEL_THRESHOLD else False)

    return {
        "is_delayed": is_delayed,
        "prediction": "Delayed" if is_delayed else "On time",
        "delay_probability": round(float(delay_probability) * 100, 2)
    }