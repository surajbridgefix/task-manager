import random
import time
import os
import threading


def find_primes(limit=50000):
    """Find all prime numbers up to the given limit."""
    
    print()
    print(
        f"[PID: {os.getpid()} | Thread: {threading.current_thread().name}]"
        "Starting Prime Number Task...")
    primes = []
    for i in range(2, limit + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    print(f"Prime Number Task Completed. Found {len(primes)} primes.")
    print()


def calculate_fibonacci(n=35):
    """Calculate the nth Fibonacci number recursively."""

    print()
    print(
        f"[PID: {os.getpid()} | Thread: {threading.current_thread().name}]"
        "Starting Fibonacci Task...")
    def fibonacci(num):
        if num <= 1:
            return num
        return fibonacci(num - 1) + fibonacci(num - 2)
    result = fibonacci(n)
    print(f"Fibonacci Task Completed. Fibonacci({n}) = {result}")
    print()


def sort_numbers(size=500000):
    """Generate random numbers and sort them."""

    print()
    print(
        f"[PID: {os.getpid()} | Thread: {threading.current_thread().name}]"
        "Starting Sorting Task...")
    numbers = [random.randint(1, 1000000) for _ in range(size)]
    numbers.sort()
    print("Sorting Task Completed.")
    print()


def process_files():
    """Fake file processing using sleep funtion."""

    print()
    print(
        f"[PID: {os.getpid()} | Thread: {threading.current_thread().name}] "
        "Starting File Processing Task...")
    for i in range(1, 6):
        print(f"Processing File {i}...")
        time.sleep(1)
    print("File Processing Task Completed.")
    print()

#================