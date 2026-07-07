import time

def measure_execution_time(function):
    """Measure the execution time of a function."""

    start_time = time.perf_counter()
    function()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time