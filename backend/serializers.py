import numpy as np


def to_native(value):
    """
    Convert numpy / pandas types to native Python types.
    """
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        return float(value)
    if isinstance(value, dict):
        return {k: to_native(v) for k, v in value.items()}
    if isinstance(value, list):
        return [to_native(v) for v in value]
    return value


def serialize_response(data: dict) -> dict:
    """
    Fully serialize nested response data.
    """
    return to_native(data)