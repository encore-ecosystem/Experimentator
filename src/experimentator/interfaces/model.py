from ..measurer import Measurer
from abc import ABCMeta, abstractmethod
from nodeflow.adapter import Adapter
from cvtk import AbstractDataset
from prologger import Logger
from pathlib import Path


class Model(Adapter, metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def load(cls, weights_path: Path):
        raise NotImplementedError()

    @abstractmethod
    def save(self, weights_path: Path):
        raise NotImplementedError()

    @abstractmethod
    def predict(self, inp):
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
