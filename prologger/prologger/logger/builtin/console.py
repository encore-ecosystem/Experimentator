from ..interface import Logger
from datetime import datetime


class ConsoleLogger(Logger):
    def _print(self, message: str, extras: str, importance: int):
        if importance >= self._importance_threshold:
            print(f"[{datetime.now().strftime("%H:%M:%S %Y/%m/%d")}][{extras}] : {message}")


__all__ = [
    "ConsoleLogger",
]
