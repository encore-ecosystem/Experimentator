from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def info(self, msg: str):
        raise NotImplementedError()

    @abstractmethod
    def warning(self, msg: str):
        raise NotImplementedError()
    
    @abstractmethod
    def error(self, msg: str):
        raise NotImplementedError()


__all__ = [
    'Logger',
]
