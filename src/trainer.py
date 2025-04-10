from prologger.prologger import Logger
from src.interfaces import Model, Dataset, Persist
from src.measurer import Measurer
from pathlib import Path


class Trainer(Persist):
    def __init__(self, train_dataset: Dataset, eval_dataset: Dataset, epochs: int = 500):
        self._num_epochs    = epochs
        self._cur_epoch     = 0
        self._train_dataset = train_dataset
        self._eval_dataset  = eval_dataset

    @classmethod
    def load(cls, path: Path) -> 'Trainer':
        raise NotImplementedError()
    
    def save(self, path: Path):
        raise NotImplementedError()

    def __call__(self, model: Model, logger: Logger, metric_manager: Measurer):
        for epoch in range(self._cur_epoch, self._num_epochs):
            # train step
            self._epoch = epoch

            # train
            logger.info(f"Trainer [epoch={self._epoch}]: Training")

            # eval
            logger.info(f"Trainer [epoch={self._epoch}]: Eval")

            # complete
            logger.info(f"Trainer [epoch={self._epoch}]: Step complete")
            yield epoch


__all__ = [
    'Trainer'
]
