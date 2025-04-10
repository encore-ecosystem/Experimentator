from ..interface import Logger
from typing import Sequence


class UnionLogger(Logger):
    def __init__(self, loggers: Sequence[Logger], importance: int = 0):
        super().__init__(importance)
        self._loggers = loggers

    def _print(self, message: str, extras: str, importance: int):
        for logger in self._loggers:
            logger._print(message, extras, importance)


__all__ = [
    "UnionLogger",
]
