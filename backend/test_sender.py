import requests
import time
import random

API_URL = "http://localhost:8000/predict"

def generate_normal_reading():
    hr = random.uniform(120.0, 165.0)
    temp = random.uniform(36.5, 37.0)
    
    # Simulated gas readings
    ch4_ppm = round(random.uniform(5.0, 15.0), 2)
    co_ppm = round(random.uniform(0.5, 5.0), 2)

    return {
        "reading": [ hr, temp],
        "ch4_ppm": ch4_ppm,
        "co_ppm": co_ppm
    }

while True:
    payload = generate_normal_reading()
    try:
        res = requests.post(API_URL, json=payload)
        print(f"✅ Sent reading: {payload} | Response: {res.status_code}", end=" ")
        print(res.json())
    except Exception as e:
        print(f"❌ Failed to send: {payload} | Error: {e}")
    time.sleep(0.1)

