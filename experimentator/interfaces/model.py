from pathlib import Path
from abc import ABCMeta, abstractmethod

from cvtk import AbstractDataset
from nodeflow.adapter import Adapter
from prologger import Logger

from experimentator import Measurer


class Model(Adapter, metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def load(cls, weights_path: Path):
        raise NotImplementedError()

    @abstractmethod
    def save(self, weights_path: Path):
        raise NotImplementedError()

    @abstractmethod
    def predict(self, input_tensor):
        raise NotImplementedError

    @abstractmethod
    def train_step(self, dataset: AbstractDataset, measurer: Measurer, logger: Logger, current_epoch: int):
        raise NotImplementedError

    @abstractmethod
    def test_step(self, dataset: AbstractDataset, measurer: Measurer, logger: Logger, current_epoch: int):
        raise NotImplementedError

    @abstractmethod
    def eval_step(self, dataset: AbstractDataset, measurer: Measurer, logger: Logger, current_epoch: int):
        raise NotImplementedError


__all__ = [
    'Model',
]
