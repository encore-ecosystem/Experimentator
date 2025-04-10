from experimentator.interfaces import Logger
from datetime import datetime


class ConsoleLogger(Logger):
    def info(self, msg: str):
        self._msg("INFO", msg)

    def warning(self, msg: str):
        self._msg("WARNING", msg)

    def error(self, msg: str):
        self._msg("ERROR", msg)

    def _msg(self, status: str, msg: str):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{status}]: {msg}")


__all__ = [
    "ConsoleLogger",
]
