import time
import numpy as np
from multiprocessing import Pool

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def parallel_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        step = 2 if i % 2 == 0 else 1
        indices = range(step, n - 1, 2)
        for j in indices:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    with Pool(2) as pool:
        left, right = pool.map(merge_sort, [arr[:mid], arr[mid:]])
    return merge(left, right)

def benchmark_sorting(n):
    arr = np.random.randint(0, 100, n).tolist()
    
    # Sequential Bubble Sort
    arr_copy = arr[:]
    start = time.time()
    bubble_sort(arr_copy)
    sequential_bubble_time = time.time() - start
    
    # Parallel Bubble Sort
    arr_copy = arr[:]
    start = time.time()
    parallel_bubble_sort(arr_copy)
    parallel_bubble_time = time.time() - start
    
    # Sequential Merge Sort
    arr_copy = arr[:]
    start = time.time()
    merge_sort(arr_copy)
    sequential_merge_time = time.time() - start
    
    # Parallel Merge Sort
    arr_copy = arr[:]
    start = time.time()
    parallel_merge_sort(arr_copy)
    parallel_merge_time = time.time() - start
    
    print(f"Sequential Bubble Sort Time: {sequential_bubble_time:.6f} seconds")
    print(f"Parallel Bubble Sort Time: {parallel_bubble_time:.6f} seconds")
    print(f"Sequential Merge Sort Time: {sequential_merge_time:.6f} seconds")
    print(f"Parallel Merge Sort Time: {parallel_merge_time:.6f} seconds")

if __name__ == "__main__":
    n = int(input("Enter the size of the array: "))
    benchmark_sorting(n)
