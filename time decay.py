import math
from typing import Union

def temporal_decay(
    t: Union[int, float],
    s0: Union[int, float],
    decay_rate: Union[int, float]
) -> float:
    """
    Tier-dependent temporal decay model.

    s(t) = s0 * e^(-λt)

    Parameters:
        t (float): Time since last valid observation
        s0 (float): Initial importance score
        decay_rate (float): Tier-specific decay constant (λ)

    Returns:
        float: Decayed importance score
    """
    if t < 0:
        raise ValueError("Time t must be non-negative")

    return s0 * math.exp(-decay_rate * t)
