from abc import ABC, abstractmethod


class Logger(ABC):
    def __init__(self, importance_threshold: int = 0):
        self._importance_threshold = importance_threshold

    def info(self, message: str, importance: int = 0):
        self._print(message, "INFO", importance)

    def warning(self, message: str, importance: int = 0):
        self._print(message, "WARNING", importance)

    def error(self, message: str, importance: int = 0):
        self._print(message, "ERROR", importance)

    def critical(self, message: str, importance: int = 0):
        self._print(message, "CRITICAL", importance)

    def debug(self, message: str, importance: int = 0):
        self._print(message, "DEBUG", importance)

    @abstractmethod
    def _print(self, message: str, extras: str, importance: int):
        raise NotImplementedError()


__all__ = [
    "Logger",
]
