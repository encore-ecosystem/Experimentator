from ..interface import Logger
from datetime import datetime
from pathlib import Path


class FileLogger(Logger):
    def __init__(self, logging_path: Path, importance: int = 0):
        super().__init__(importance)
        logging_path.mkdir(parents=True, exist_ok=True)
        self._file_path = logging_path / datetime.now().strftime("%Y-%m-%d %H-%M-%S.log")
        self._file_path.touch()

    def _print(self, message: str, extras: str, importance: int):
        if importance >= self._importance_threshold:
            with open(self._file_path, "a") as f:
                f.write(f"[{datetime.now().strftime("%H:%M:%S %Y/%m/%d")}][{extras}] : {message}\n")


__all__ = [
    "FileLogger",
]