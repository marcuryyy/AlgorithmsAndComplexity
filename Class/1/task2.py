from memory_profiler import profile
import time
import psutil
import os
k = int(input())
process = psutil.Process(os.getpid())
memory_info = process.memory_info()
now = time.perf_counter()
@profile
def get_answer(k: int):
    field: list[int] = [0 for _ in range(10)]
    counter: int = 0
    for i in range(4):
        string: str = input()
        for char in string:
            if char == '.':
                field[0] += 1
            else:
                field[int(char)] += 1

    for t in range(1, 10):
        current_amount = field[t]
        if k * 2 >= current_amount != 0:
            counter += 1
    return counter


print(get_answer(k))
print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"Memory usage: {memory_info.rss / 1024 / 1024} MB")