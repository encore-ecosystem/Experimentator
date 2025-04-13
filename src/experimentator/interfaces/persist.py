from abc import ABC, abstractmethod
from pathlib import Path


class Persist(ABC):
    @classmethod
    @abstractmethod
    def load(cls, src_path: Path) -> 'Persist':
        raise NotImplementedError

    @abstractmethod
    def save(self, dst_path: Path):
        raise NotImplementedError


__all__ = [
    'Persist'
]
