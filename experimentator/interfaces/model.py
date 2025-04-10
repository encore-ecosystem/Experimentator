from pathlib import Path
from abc import ABCMeta, abstractmethod
from nodeflow.adapter import Adapter


class Model(Adapter, metaclass=ABCMeta):
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
