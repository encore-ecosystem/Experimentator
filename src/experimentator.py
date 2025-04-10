from experimentator.interfaces import Model
from .logger.logger import Logger
from .measurer import Measurer
from .trainer import Trainer

from pathlib import Path
from deque import deque

import os


class ExperimentatorClient:
    def __init__(self, experiments_path: Path):
        self._tasks = deque()

        self._experiments_path = experiments_path
        self._experiments_path.mkdir(parents=True, exist_ok=True)

    def run_experiment(
        self,
        trainer         : Trainer,
        logger          : Logger,
        measurer        : Measurer,
        experiment_name : str  = "experiment",
        checkpoint_step : int  = 5,
        resume          : bool = True,
    ):
        #
        assert checkpoint_step > 0

        experiment_path = self._experiments_path
        if resume:
            if (self._experiments_path / experiment_name).exists():
                logger.info("Resuming experiment")
                experiment_path /= experiment_name
                self._model.load()
                trainer.load_config()
            else:
                logger.err(
                    f"Unable to find experiment: {self._experiments_path / experiment_name}"
                )
                return False
        else:
            experiment_path /= (
                f"{experiment_name}_{len(os.listdir(experiment_path)) + 1}"
            )

        #
        logger.info(f"Experiment path is: {experiment_path}")

        for epoch in trainer(
            model=self._model, logger=logger, metric_manager=self._metric_manager
        ):
            if epoch % checkpoint_step == 0:
                # checkpoint
                ...

        #
        logger.info(f"Experiment {experiment_name} complete!")


__all__ = [
    "ExperimentatorClient",
]
