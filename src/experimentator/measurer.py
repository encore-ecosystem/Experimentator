from matplotlib import pyplot as plt
from pathlib import Path


class Measurer:
    def __init__(self):
        self.epoch_metrics = {}
        self.raw_metrics = {}

    def end_epoch(self):
        for metric in self.raw_metrics:
            temp = self.raw_metrics[metric]
            self.epoch_metrics[metric] = self.epoch_metrics.get(metric, []) + [sum(temp) / len(temp)]
            self.raw_metrics[metric] = []

    def update(self, metric: str, value: float):
        self.raw_metrics[metric] = self.raw_metrics.get(metric, []) + [value]

    def get_raw(self, metric: str) -> list[float]:
        return self.raw_metrics.get(metric, [])

    def get(self, metric: str) -> list[float]:
        return self.epoch_metrics.get(metric, [])

    def get_with_epochs(self, metric: str) -> tuple[range, list[float]]:
        metric = self.get(metric)
        return range(len(metric)), metric

    def get_raw_with_epochs(self, metric: str) -> tuple[range, list[float]]:
        metric = self.get_raw(metric)
        return range(len(metric)), metric

    def get_metrics(self) -> list[str]:
        return list(self.raw_metrics.keys())

    def make_plots(self, plots_path: Path, current_epoch: int):
        for metric in self.get_metrics():
            path = plots_path / metric
            path.mkdir(parents=True, exist_ok=True)

            plt.Figure()
            plt.title(metric.replace('_', ' ').capitalize())
            plt.plot(*self.get_with_epochs(metric))
            plt.savefig(path / f'{current_epoch}.png')
            plt.close()



__all__ = [
    "Measurer"
]
