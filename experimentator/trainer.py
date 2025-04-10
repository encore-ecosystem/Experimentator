from prologger import Logger
from cvtk import AbstractDataset
from experimentator.interfaces import Model, Persist
from experimentator.measurer import Measurer
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Trainer(Persist):
    train_dataset: AbstractDataset
    test_dataset: AbstractDataset
    eval_dataset: AbstractDataset
    epochs: int
    checkpoint_step : int
    resume: bool
    measurer: Measurer
    logger : Logger

    @classmethod
    def load(cls, path: Path) -> 'Trainer':
        raise NotImplementedError()
    
    def save(self, path: Path):
        raise NotImplementedError()

    def train(self, model: Model, logger: Logger, metric_manager: Measurer):
        raise NotImplementedError()


__all__ = ["Trainer"]
