from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from app.core.buffer import add_reading
from app.core.predictor import predict_fatigue
from app.utils.logger import log_data
from app.auth.routes import router as auth_router

app = FastAPI(
    title="SPY Helmet Fatigue API",
    version="1.0",
    description="Real-time fatigue prediction for miners using 2-sensor input ⚡"
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for now; restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

latest_prediction = None

# ✅ Input schema: Expect 5 features + CH4 + CO
class ReadingInput(BaseModel):
    reading: List[float]  # [x, y, z, HR, TEMP]
    ch4_ppm: float
    co_ppm: float

@app.get("/")
def root():
    return {"message": "✅ SPY Helmet Fatigue API is running (2-input + gas sensors)"}

@app.post("/predict")
async def predict(input_data: ReadingInput):
    global latest_prediction
    try:
        reading = input_data.reading

        # Validate length = 2
        if len(reading) != 2:
            raise HTTPException(status_code=400, detail="Each reading must contain exactly 2 values: [ HR, TEMP]")

        # Add to buffer
        sequence = add_reading(reading)  # should return (100, 5) or None

        if sequence is None:
            return {
                "status": "collecting",
                "message": "Waiting for 100 readings..."
            }

        # Predict
        result = predict_fatigue(sequence)

        # Log it
        log_data(reading, result["prediction"], None)

        # Store for frontend
        latest_prediction = {
            "prediction": result["prediction"],
            "confidence": f"{result['confidence']:.2f}%",
            "raw_scores": result["raw_scores"],
            "heart_rate": reading[0],
            "body_temp": reading[1],
            "ch4_ppm": input_data.ch4_ppm,
            "co_ppm": input_data.co_ppm
        }

        return latest_prediction

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/live_predict")
async def live_prediction():
    global latest_prediction
    if latest_prediction is None:
        return {
            "status": "collecting",
            "message": "Waiting for 100 readings..."
        }
    return latest_prediction

# Mount auth routes
app.include_router(auth_router)
