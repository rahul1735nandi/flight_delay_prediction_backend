import joblib

model = joblib.load("models/flight_delay_prediction_model_v3.pkl")
prediction_features = joblib.load("models/prediction_features.pkl")

print("Model loaded: V3")
print("Total features:", len(prediction_features))