"""Vector store scaffold."""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Sequence


class VectorStore:
    def __init__(self, metric: str = "cosine") -> None:
        # metric must be "cosine" or "euclidean", otherwise raise ValueError.
        # Initialize empty internal state: an empty records dict,
        # a dimension field set to None, and an auto-increment id counter.
        if metric not in ("cosine", "euclidean"):
            raise ValueError('metric must be "cosine" or "euclidean"')
        self.metric = metric
        self.records: Dict[str, Dict[str, Any]] = {}
        self.dimension: Optional[int] = None
        self._id_counter = 0

    def create(self, vector, metadata=None, *, id=None) -> str:
        raise NotImplementedError

    def read(self, id) -> dict:
        raise NotImplementedError

    def update(self, id, *, vector=None, metadata=None) -> dict:
        raise NotImplementedError

    def delete(self, id) -> None:
        raise NotImplementedError

    def search(self, query, k=5, *, filter=None) -> list:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, id) -> bool:
        raise NotImplementedError

    def to_dict(self) -> dict:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, data) -> "VectorStore":
        raise NotImplementedError
