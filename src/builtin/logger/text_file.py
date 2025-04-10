from experimentator.interfaces import Logger
from pathlib import Path
from datetime import datetime


class TextFileLogger(Logger):
    def __init__(self, log_file_path: Path):
        self.log_file_path = log_file_path

        self.log_file_path.parent().mkdir(exists_ok=True, parents=True)
        self.log_file_path.touch()

    def info(self, msg: str):
        self._msg("INFO", msg)

    def warn(self, msg: str):
        self._msg("WARN", msg)

    def err(self, msg: str):
        self._msg("ERR", msg)

    def _msg(self, status: str, msg: str):
        with open(self.log_file_path, "a") as file:
            file.write(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{status}]: {msg}"
            )


__all__ = [
    "TextFileLogger",
]
