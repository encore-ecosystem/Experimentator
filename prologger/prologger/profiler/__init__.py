from typing import Callable

import time

class Profiler:
    def __init__(self):
        self._enable = True
        self.info = {}

    def disable(self):
        self._enable = False

    def enable(self):
        self._enable = True

    def add_measure(self, func_name: str, measurement_group: str, time_ms: float):
        if measurement_group not in self.info:
            self.info[measurement_group] = {}
        self.info[measurement_group][func_name] = self.info[measurement_group].get(func_name, []) + [time_ms]

    def __call__(self, include_to_measurements: bool = True, measurements_group: str = 'default'):
        def decorator(func: Callable):
            def wrapper(*args, **kwargs):
                start = time.time()
                res = func(*args, **kwargs)
                end = time.time()
                profiler.add_measure(f"{__file__} : {func.__qualname__}", measurements_group, (end - start) * 1000)
                return res
            return wrapper if include_to_measurements else func
        return decorator

    def print_result(self):
        for group in self.info:
            print(f"{f"[group: {group}]":=^128}")
            for func in self.info[group]:
                print(f"{func}")
                measurements = self.info[group][func]
                print(f"Average time is: {sum(measurements) / len(measurements) : 7f} ms.")
                print(f"Minimal time is: {min(measurements) : 7f} ms.")
                print(f"Maximum time is: {max(measurements) : 7f} ms.")

                print()

profiler = Profiler()


__all__ = [
    'profiler',
]
