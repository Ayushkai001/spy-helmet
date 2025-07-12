import requests
import random

# Generate test data matching model shape (100 steps of 5 features)
sequence = [
    [
        random.uniform(-10, 10),   # X
        random.uniform(-10, 10),   # Y
        random.uniform(-10, 10),   # Z
        random.uniform(100, 105),  # HR
        random.uniform(33.0, 34.0) # TEMP
    ]
    for _ in range(100)
]

response = requests.post("http://localhost:8000/predict", json={"sequence": sequence})
print(response.json())
