import numba  # ✅ FIX: Explicitly import numba
from numba import cuda
import numpy as np
import time

# Define CUDA kernel for vector addition
@cuda.jit
def vector_add_kernel(a, b, c):
    idx = cuda.grid(1)
    if idx < a.size:
        c[idx] = a[idx] + b[idx]

# Define CUDA kernel for finding maximum element
@cuda.jit
def max_element_kernel(arr, max_val):
    idx = cuda.grid(1)
    shared_mem = cuda.shared.array(shape=(128,), dtype=numba.int32)  # ✅ FIX: Explicit dtype

    tid = cuda.threadIdx.x
    if idx < arr.size:
        shared_mem[tid] = arr[idx]
    else:
        shared_mem[tid] = 0  # Padding

    cuda.syncthreads()

    # Parallel reduction for max
    i = 64
    while i > 0:
        if tid < i:
            shared_mem[tid] = max(shared_mem[tid], shared_mem[tid + i])
        cuda.syncthreads()
        i //= 2

    if tid == 0:
        cuda.atomic.max(max_val, 0, shared_mem[0])

# Function to perform vector addition using CUDA
def vector_addition(a, b):
    N = len(a)
    c = np.zeros(N, dtype=np.int32)

    d_a = cuda.to_device(a)
    d_b = cuda.to_device(b)
    d_c = cuda.device_array(N, dtype=np.int32)

    threads_per_block = 128
    blocks_per_grid = (N + threads_per_block - 1) // threads_per_block

    start_time = time.time()
    vector_add_kernel[blocks_per_grid, threads_per_block](d_a, d_b, d_c)
    cuda.synchronize()
    end_time = time.time()

    d_c.copy_to_host(c)
    error = np.sum(c - (a + b))

    print(f"1. Error : {error}")
    print(f"   Time Elapsed: {end_time - start_time:.6f}")

    return c

# Function to find the maximum element using CUDA
def find_max_element(arr):
    N = len(arr)
    max_val = np.zeros(1, dtype=np.int32)

    d_arr = cuda.to_device(arr)
    d_max_val = cuda.to_device(max_val)

    threads_per_block = 128
    blocks_per_grid = (N + threads_per_block - 1) // threads_per_block

    start_time = time.time()
    max_element_kernel[blocks_per_grid, threads_per_block](d_arr, d_max_val)
    cuda.synchronize()
    end_time = time.time()

    max_val = d_max_val.copy_to_host()[0]

    print(f"2. The maximum element is : {max_val}")
    print(f"   The time required : {end_time - start_time:.6f}")

# Main Execution
if __name__ == "__main__":
    N = 10**6

    np.random.seed(42)
    a = np.random.randint(0, 100, size=N, dtype=np.int32)
    b = np.random.randint(0, 100, size=N, dtype=np.int32)

    c = vector_addition(a, b)
    find_max_element(c)
