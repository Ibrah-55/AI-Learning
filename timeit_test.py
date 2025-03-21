import numpy as np
import timeit

np.random.seed(0)

def rec_compute(n):
    out = np.empty(len(n))
    for i in range(len(n)):
        out[i] = 1.0 / n[i]
    return out
n = np.random.randint(1, 100, size=5*1000)
print(rec_compute(n))

array_massive = np.random.randint(1, 100, size=5*100000)

r = rec_compute(array_massive)
time_taken = timeit.timeit(lambda: rec_compute(array_massive), number=1)
print(f"Time taken: {time_taken} seconds")
print("Big array: \n", r)