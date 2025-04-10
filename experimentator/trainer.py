from prologger import Logger
from experimentator.interfaces import Model, Dataset, Persist
from experimentator.measurer import Measurer
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Trainer(Persist):
    train_dataset: Dataset
    test_dataset: Dataset
    eval_dataset: Dataset
    epochs: int
    measurer: Measurer
    resume: bool
    checkpoint_step : int

    @classmethod
    def load(cls, path: Path) -> 'Trainer':
        raise NotImplementedError()
    
    def save(self, path: Path):
        raise NotImplementedError()

    def train(self, model: Model, logger: Logger, metric_manager: Measurer):
        raise NotImplementedError()


__all__ = ["Trainer"]
