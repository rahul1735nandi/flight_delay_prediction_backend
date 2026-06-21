import joblib

MODEL_THRESHOLD = 0.50

try:
    model = joblib.load("models/flight_delay_prediction_rf_model.pkl")
    feature_columns = joblib.load("models/feature_columns.pkl")

    print("\nRandom Forest model loaded")
    print("Threshold: ", MODEL_THRESHOLD)
    print("Feature count:", len(feature_columns))

except Exception as e:
    raise RuntimeError(f"Model loading failed: {e}")
