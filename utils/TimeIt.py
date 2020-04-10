import math
from datetime import datetime


class TimeIt:
    def __init__(self, n: int = 10) -> None:
        self.n_runs = n

    def __call__(self, original_func):
        def wrappee(*args, **kwargs):
            measurements = []
            for _ in range(self.n_runs):
                startTime = datetime.now()
                original_func(*args, **kwargs)
                elapsedTime = datetime.now() - startTime
                measurements.append(elapsedTime.microseconds)

            mean = sum(measurements) / len(measurements)
            std = math.sqrt(sum((x - mean) ** 2 for x in measurements) / len(measurements))

            print(f"[timeit] run {original_func} for {self.n_runs} run with mean of {mean} and std of {std}")

        return wrappee