import time
import numpy as np
from functools import wraps
from numba import jit

# Check number of threads allowed in Python
import threading

print(threading.active_count())

# Check number of processes allowed in Python
import multiprocessing

print(multiprocessing.cpu_count())

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time

@timefn
def primes(N=1000000):
    numbers = np.ones(N, dtype=np.uint8)  # initialize the boolean array
    for i in range(2, N):
        if numbers[i] == 0:  # has previously been crossed off
            continue
        else:  # it is a prime, cross off all multiples
            x = i + i
            while x < N:
                numbers[x] = 0
                x += i
    # return all primes, as indicated by all boolean positions that are one
    return np.nonzero(numbers)[0][2:]

print(primes())
# start_time = time.time()

# for _ in range(100000):
#     primes()

# end_time = time.time()

# total_latency = end_time - start_time
# print(f"Total latency for 100,000 requests: {total_latency} seconds")