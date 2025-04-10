from experimentator.interfaces import Model, Persist
from typing import Sequence
from pathlib import Path

import pickle


class Pipeline(Persist):
    def __init__(self, models: Sequence[Model]):
        self._models = models

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
