import time
import psutil
import os
N, M, MOD = map(int, input().split())


process = psutil.Process(os.getpid())
memory_info = process.memory_info()

def get_answer(N: int, M: int, MOD: int):
    list_a_i: list[int] = [0 for _ in range(N + 1)]
    list_x_i: list[int] = [0 for _ in range(M)]

    for i in range(N+1):
        list_a_i[i] = int(input())

    for i in range(M):
        list_x_i[i] = int(input())

    list_a_length: int = len(list_a_i)
    result = []
    for x in list_x_i:
        total_sum = list_a_i[0]
        for i in range(1, list_a_length):
            total_sum = total_sum * x + list_a_i[i]
        result.append(total_sum % MOD)
    return "\n".join(str(x) for x in result)


get_answer(N, M, MOD)
print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"Memory usage: {memory_info.rss / 1024 / 1024} MB")
