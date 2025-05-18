from .interfaces.persist import Persist
from .interfaces.model import Model
from typing import Sequence
from pathlib import Path
from prologger import Logger
import pickle


class Pipeline(Persist):
    def __init__(self, models: Sequence[Model]):
        self._models = models

    def __len__(self) -> int:
        return len(self._models)

    def __iter__(self):
        return self._models.__iter__()

    def train(self, logger: Logger):
        for model in self._models:
            model.tra

    @classmethod
    def load(cls, src_path: Path) -> 'Pipeline':
        with open(src_path, "rb") as file:
            return pickle.load(file)

    def save(self, dst_path: Path):
        with open(dst_path, "wb") as file:
            pickle.dump(self, file)


__all__ = [
    'Pipeline'
]
