import time
from memory_profiler import memory_usage
import os

m_start = memory_usage()[0]


def is_square(number):
    left = 1
    right = number // 2

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == n:
            return True
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1
    return False


now = time.perf_counter()
with open('input.txt') as f:
    N = int(f.readline())
    for i in range(N):
        n = int(f.readline())
        print(len(str(n)))
        if is_square(n):
            print(i + 1)

print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"{memory_usage()[0] - m_start} Mb")
