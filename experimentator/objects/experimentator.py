from .experiment import Experiment
from pathlib import Path


class ExperimentatorClient:
    def __init__(self, experiments_path: Path):
        self._experiments = []
        self._experiments_path = experiments_path
        self._experiments_path.mkdir(parents=True, exist_ok=True)

    def add_experiment(self, experiment: Experiment):
        self._experiments.append(experiment)

    def load_experiment(self, experiment_name: str):
        experiment = Experiment.load(self._experiments_path / experiment_name)
        self.add_experiment(experiment)

    def run_experiments(self):
        while len(self._experiments) > 0:
            experiment = self._experiments.pop(0)
            self.run_experiment(experiment)

    def run_experiment(self, experiment: Experiment):
        raise NotImplementedError()


__all__ = [
    "ExperimentatorClient",
]
