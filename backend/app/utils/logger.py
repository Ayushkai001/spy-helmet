# app/utils/logger.py

import csv
import os
from datetime import datetime

# Path to store logs
LOG_FILE = "app/logs/prediction_logs.csv"

# Ensure directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_data(reading, prediction, user_id=None):
    """
    Logs a reading and its prediction to CSV file.
    reading: list of 5 floats
    prediction: predicted label (str)
    user_id: optional user identifier
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Prepare row
    row = [now] + reading + [prediction, user_id if user_id else ""]

    # Write to CSV
    write_header = not os.path.exists(LOG_FILE)
    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            header = ["timestamp", "x", "y", "z", "hr", "temp", "prediction", "user_id"]
            writer.writerow(header)
        writer.writerow(row)
