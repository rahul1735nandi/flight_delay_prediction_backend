from fastapi import FastAPI

from request_model import FlightRequest
from model_loader import model
from prediction_service import prepare_input_data
from response_model import PredictionResponse

app = FastAPI()

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

    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)
    is_delayed = int(prediction[0])
    delay_probability = round(float(probability[0][1]) * 100, 2)

    return {
        "is_delayed": is_delayed,
        "prediction": "Delayed" if is_delayed == 1 else "On time",
        "delay_probability": delay_probability
    }