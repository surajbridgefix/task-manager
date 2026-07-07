from sequential import run_sequential
from multithreading import run_multithreading
from multiprocessing_demo import run_multiprocessing
from timer import measure_execution_time

def compare_all():

    print("==================================================")
    print("              PERFORMANCE COMPARISON              ")
    print("==================================================")

    sequential_time = measure_execution_time(run_sequential)
    threading_time = measure_execution_time(run_multithreading)
    multiprocessing_time = measure_execution_time(run_multiprocessing)

    print("\n=================== RESULTS ====================")

    print("Sequential      :", round(sequential_time, 5), "seconds")
    print("Multithreading  :", round(threading_time, 5), "seconds")
    print("Multiprocessing :", round(multiprocessing_time, 5), "seconds")

    fastest = min(sequential_time, threading_time, multiprocessing_time)

    if fastest == sequential_time:
        print("\nFastest : Sequential")
    elif fastest == threading_time:
        print("\nFastest : Multithreading")
    else:
        print("\nFastest : Multiprocessing")