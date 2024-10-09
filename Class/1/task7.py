import time
import psutil
import os

N = int(input())
weights = list(map(int, input().split()))

process = psutil.Process(os.getpid())
now = time.perf_counter()

def get_min_diff(rocks: list[int]):
    total_sum: int = sum(rocks)
    possible_sums: list[int] = [0 for _ in range(total_sum)]
    sums_length: int = len(possible_sums)
    possible_sums[0] = 1
    answer = float('inf')
    for rock in rocks:
        for j in range(sums_length - 1, rock - 1, -1):
            if possible_sums[j] != 1:
                if j == rock:
                    possible_sums[j] = 1
                else:
                    if j - rock >= 0:
                        possible_sums[j] = possible_sums[j - rock]
    print(possible_sums)
    for i in range(total_sum):
        if possible_sums[i] == 1:
            answer = min(answer, abs(i - (total_sum - i)))
    return answer

memory_info = process.memory_info()
print(get_min_diff(weights))

# print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
# print(f"Memory usage: {memory_info.rss / 1024 / 1024} MB")
