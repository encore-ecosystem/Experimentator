from pathlib import Path
from abc import ABC, abstractmethod


class Model(ABC):
    @classmethod
    @abstractmethod
    def load(cls, weights_path: Path):
        raise NotImplementedError()

    @abstractmethod
    def save(self, weights_path: Path):
        raise NotImplementedError()


__all__ = [
    'Model',
]
