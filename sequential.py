from tasks import find_primes, calculate_fibonacci, sort_numbers, process_files

def run_sequential():
    """Execute all tasks one after another."""

    print("==================================================")
    print("           SEQUENTIAL EXECUTION STARTED           ")
    print("==================================================")
    find_primes()
    calculate_fibonacci()
    sort_numbers()
    process_files()
    print("==================================================")
    print("          SEQUENTIAL EXECUTION COMPLETED          ")
    print("==================================================")