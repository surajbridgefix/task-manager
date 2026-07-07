import os
from sequential import run_sequential
from multithreading import run_multithreading
from multiprocessing_demo import run_multiprocessing
from timer import measure_execution_time
from compare import compare_all


def main():
    os.system('clear')
    while True:
        print("==================================================")
        print("              TASK MANAGER SIMULATOR              ")
        print("==================================================")
        print("1. Sequential Execution")
        print("2. Multithreading")
        print("3. Multiprocessing")
        print("4. Compare All")
        print("5. Exit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            execution_time = measure_execution_time(run_sequential)
            print("\nExecution Time:", round(execution_time, 5), "seconds")
            print("===============================================")
            input("\nPress Enter to return to the Main Menu...")
        elif choice == "2":
            execution_time = measure_execution_time(run_multithreading)
            print("\nExecution Time:", round(execution_time, 5), "seconds")
            print("===============================================")
            input("\nPress Enter to return to the Main Menu...")
        elif choice == "3":
            execution_time = measure_execution_time(run_multiprocessing)
            print("\nExecution Time:", round(execution_time, 5), "seconds")
            print("===============================================")
            input("\nPress Enter to return to the Main Menu...")
        elif choice == "4":
            os.system('clear')
            compare_all()
            print("===============================================")
            input("\nPress Enter to return to Main Menu...")
        elif choice == "5":
            os.system('clear')
            print("\nThank you for using Task Manager Simulator.")
            break
        else:
            print("\nInvalid Choice!")
            input("\nPress Enter to return to the Main Menu...")

if __name__ == "__main__":
    main()