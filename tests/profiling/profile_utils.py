import inspect
from line_profiler import LineProfiler


def profile_function(func, *args, **kwargs):
    profiler = LineProfiler()
    profiler.add_function(func)

    def profiled_func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Error during {func.__name__}: {e}")

    profiler.enable_by_count()
    profiled_func(*args, **kwargs)
    profiler.disable_by_count()
    profiler.print_stats()
