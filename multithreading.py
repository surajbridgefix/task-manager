import threading
from tasks import find_primes, calculate_fibonacci, sort_numbers, process_files

def run_multithreading():

    print("==================================================")
    print("         MULTITHREADING EXECUTION STARTED         ")
    print("==================================================")
    
    thread1 = threading.Thread(target = find_primes)
    thread2 = threading.Thread(target = calculate_fibonacci)
    thread3 = threading.Thread(target = sort_numbers)
    thread4 = threading.Thread(target = process_files)
    
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    
    print("==================================================")
    print("        MULTITHREADING EXECUTION COMPLETED        ")
    print("==================================================")