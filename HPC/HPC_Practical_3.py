import multiprocessing
import random

def find_min(arr, result, index):
    """Finds the minimum value in the array."""
    min_val = min(arr)
    result[index] = min_val
    print(f"Process ID: {multiprocessing.current_process().pid}, Min Value: {min_val}")

def find_max(arr, result, index):
    """Finds the maximum value in the array."""
    max_val = max(arr)
    result[index] = max_val
    print(f"Process ID: {multiprocessing.current_process().pid}, Max Value: {max_val}")

def find_avg(arr, result, index):
    """Finds the average value in the array."""
    avg_val = sum(arr) / len(arr)
    result[index] = avg_val
    print(f"Process ID: {multiprocessing.current_process().pid}, Average Value: {avg_val}")

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))

    if n <= 0:
        print("Array size must be greater than zero!")
        exit(1)

    arr = [random.randint(0, 100) for _ in range(n)]  # Generate random numbers between 0 and 100

    print("\nArray elements are:", arr)

    # Shared memory array for storing results from multiple processes
    manager = multiprocessing.Manager()
    result = manager.list([None] * 3)  # Store min, max, avg

    # Creating processes
    p1 = multiprocessing.Process(target=find_min, args=(arr, result, 0))
    p2 = multiprocessing.Process(target=find_max, args=(arr, result, 1))
    p3 = multiprocessing.Process(target=find_avg, args=(arr, result, 2))

    # Starting processes
    p1.start()
    p2.start()
    p3.start()

    # Waiting for processes to finish
    p1.join()
    p2.join()
    p3.join()

    print("\nResults:")
    print(f"Minimum Value = {result[0]}")
    print(f"Maximum Value = {result[1]}")
    print(f"Average Value = {result[2]:.2f}")
