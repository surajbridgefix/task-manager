import multiprocessing
from tasks import find_primes, calculate_fibonacci, sort_numbers, process_files

def run_multiprocessing():

    print("==================================================")
    print("         MULTIPROCESSING EXECUTION STARTED        ")
    print("==================================================")

    process1 = multiprocessing.Process(target=find_primes   )
    process2 = multiprocessing.Process(target=calculate_fibonacci)
    process3 = multiprocessing.Process(target=sort_numbers)
    process4 = multiprocessing.Process(target=process_files)

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
   
    print("==================================================")
    print("        MULTIPROCESSING EXECUTION COMPLETED       ")
    print("==================================================")