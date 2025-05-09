import time
from functools import wraps

from tabulate import tabulate

# Global log store
execution_log: dict[str, dict] = dict()


def timer_decorator(cls):
    """
    Class decorator to time all method calls and log them.
    """
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            # Wrap the method
            original_method = attr_value

            @wraps(original_method)
            def wrapped_method(
                self, *args, __method=original_method, __name=attr_name, **kwargs
            ):
                f_name: str = f"{cls.__name__}.{__name}"
                start: int = time.perf_counter_ns()
                result = __method(self, *args, **kwargs)
                end: int = time.perf_counter_ns()
                elapsed: float = (end - start) * 1e-9
                old_elapsed: float = execution_log.get(f_name, {"Time (s)": 0}).get("Time (s)")

                # if old_elapsed < elapsed:
                # Log the call
                execution_log[f_name] = {
                    "Function": f"{cls.__name__}.{__name}",
                    "Time (s)": elapsed + old_elapsed,
                    "Args": (
                        f"{repr(args)[:50]}..."
                        if len(repr(args)) > 50
                        else repr(args)
                    ),
                    "Kwargs": (
                        f"{repr(kwargs)[:50]}..."
                        if len(repr(kwargs)) > 50
                        else repr(kwargs)
                    ),
                }

                return result
            setattr(cls, attr_name, wrapped_method)
    return cls


def print_execution_log():
    """
    Pretty-prints the execution log using tabulate.
    """
    if execution_log:
        print(tabulate(list(execution_log.values()), headers="keys", tablefmt="grid"))
        print(f"\nTotal time (s) -> {sum(e['Time (s)'] for e in execution_log.values())}")
    else:
        print("No methods have been timed yet.")
