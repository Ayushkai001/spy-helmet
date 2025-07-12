# app/core/buffer.py

import numpy as np

# Global buffer to store readings
BUFFER_SIZE = 100
buffer = []

def add_reading(reading: list[float]) -> np.ndarray | None:
    """
    Adds a single reading to the buffer.
    Returns a full (100, 5) numpy array when ready, else None.
    """
    global buffer

    if len(reading) != 2:
        raise ValueError("Each reading must have exactly 2 values.")

    buffer.append(reading)

    # Keep buffer size to last 100 only
    if len(buffer) > BUFFER_SIZE:
        buffer.pop(0)

    if len(buffer) == BUFFER_SIZE:
        return np.array(buffer).astype(np.float32)
    else:
        return None
