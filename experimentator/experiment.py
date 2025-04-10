from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from experimentator import Pipeline, Trainer
from experimentator.interfaces import Persist

@dataclass
class Experiment(Persist):
    name     : str
    pipeline : Pipeline
    trainers : Sequence[Trainer]

    @classmethod
    def load(cls, src_path: Path) -> 'Experiment':
        raise NotImplementedError
        # name     = src_path.name
        # pipeline = Pipeline.load(src_path / 'pipeline.pcl')
        # trainer  = Trainer.load(src_path / 'trainer.pcl')
        #
        # return Experiment(name, pipeline, trainer)

    def save(self, dst_path: Path):
        experiment_path = dst_path / self.name
        experiment_path.mkdir(exist_ok=True)

        self.pipeline.save(experiment_path / 'pipeline.pcl')
        self.trainer.save(experiment_path / 'trainer.pcl')

__all__ = [
    'Experiment'
]
