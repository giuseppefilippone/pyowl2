import time
from functools import wraps

from tabulate import tabulate

# Global log store
execution_log: dict[str, dict] = dict()


def timer_decorator(cls):
    """
    This class decorator instruments a class by wrapping its public, non-dunder methods to measure and log their execution performance. Upon application, it iterates through the class's attributes, identifying callable members that do not start with double underscores, and replaces them with a wrapper that records the elapsed time using high-resolution timers. The wrapper accumulates the total execution time for each method in a global dictionary named `execution_log`, associating it with the fully qualified method name and truncated representations of the passed arguments and keyword arguments. While the decorator modifies the global log state and the class's method attributes, it ensures the original method's behavior and return values are preserved.

    :param cls: The class whose methods will be timed and logged.
    :type cls: typing.Any
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
    """Formats and displays the current execution log as a readable grid table using the tabulate library. The output includes the function name, execution time, arguments, and keyword arguments for each recorded method call, followed by a summary of the total elapsed time across all entries. If the execution log is empty, the function prints a message indicating that no timing data is available. This function performs side effects by writing to standard output and does not return a value."""

    if execution_log:
        print(tabulate(list(execution_log.values()), headers="keys", tablefmt="grid"))
        print(f"\nTotal time (s) -> {sum(e['Time (s)'] for e in execution_log.values())}")
    else:
        print("No methods have been timed yet.")
