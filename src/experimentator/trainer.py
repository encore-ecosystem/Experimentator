from prologger import Logger
from cvtk.interfaces import AbstractDataset
from .measurer import Measurer
from .interfaces import Model, Persist
from pathlib import Path
from dataclasses import dataclass
from tqdm import tqdm


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

    def train(self, model: 'Model'):
        for epoch in tqdm(range(self.epochs), desc=f"Train step of: {model}"):
            model.train_step(self.train_dataset, self.measurer, self.logger, epoch)

        for epoch in tqdm(range(self.epochs), desc=f"Test step of: {model}"):
            model.test_step(self.train_dataset, self.measurer, self.logger, epoch)

        for epoch in tqdm(range(self.epochs), desc=f"Eval step of: {model}"):
            model.eval_step(self.train_dataset, self.measurer, self.logger, epoch)


__all__ = [
    "Trainer"
]
