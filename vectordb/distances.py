"""Distance and similarity functions for vector operations."""

import math
from typing import Sequence


def cosine_similarity(a: Sequence[float], b: Sequence[float]) -> float:
    """Cosine similarity, range [-1, 1].

    Examples: identical vectors -> 1.0; orthogonal -> 0.0; opposite -> -1.0.

    Args:
        a: First sequence of floats.
        b: Second sequence of floats.

    Returns:
        Cosine similarity between a and b.

    Raises:
        ValueError: If len(a) != len(b), if either is empty, or if either
            vector has zero magnitude (cosine is undefined for a zero vector).
    """
    if len(a) != len(b):
        raise ValueError("Sequences must have the same length")
    if len(a) == 0:
        raise ValueError("Sequences must not be empty")

    dot_product = sum(x * y for x, y in zip(a, b))
    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(y * y for y in b))

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cosine similarity is undefined for zero vectors")

    return dot_product / (magnitude_a * magnitude_b)


def euclidean_distance(a: Sequence[float], b: Sequence[float]) -> float:
    """Euclidean (L2) distance.

    Example: [0,0] to [3,4] -> 5.0; identical -> 0.0.

    Args:
        a: First sequence of floats.
        b: Second sequence of floats.

    Returns:
        Euclidean distance between a and b.

    Raises:
        ValueError: If len(a) != len(b) or if either is empty.
    """
    if len(a) != len(b):
        raise ValueError("Sequences must have the same length")
    if len(a) == 0:
        raise ValueError("Sequences must not be empty")

    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
