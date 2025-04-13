from dataclasses import dataclass
from prologger import Logger
from pathlib import Path
from typing import Sequence

from .pipeline import Pipeline
from .trainer import Trainer
from .interfaces import Persist

@dataclass
class Experiment(Persist):
    name     : str
    pipeline : Pipeline
    trainers : Sequence[Trainer]
    logger   : Logger

    @classmethod
    def load(cls, src_path: Path) -> 'Experiment':
        raise NotImplementedError

    def save(self, dst_path: Path):
        experiment_path = dst_path / self.name
        experiment_path.mkdir(exist_ok=True)

        self.pipeline.save(experiment_path / 'pipeline.pcl')
        # self.trainer.save(experiment_path / 'trainer.pcl')

__all__ = [
    'Experiment'
]
