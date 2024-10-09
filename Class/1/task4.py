from memory_profiler import profile
import time
import psutil
import os

N_a, N_b = map(int, input().split())
first_list: list[int] = [0 for _ in range(N_a)]
second_List: list[int] = [0 for _ in range(N_b)]
process = psutil.Process(os.getpid())
memory_info = process.memory_info()
for i in range(N_a):
    first_list[i] = int(input())

for i in range(N_b):
    second_List[i] = int(input())

now = time.perf_counter()

@profile
def get_answer(first_list: list[int], second_List: list[int]):
    first_list_pointer: int = 0
    second_list_pointer: int = 0

    first_list_length: int = len(first_list)
    second_list_length: int = len(second_List)

    counter: int = 0

    while True:
        if first_list_pointer < first_list_length and second_list_pointer < second_list_length:
            if first_list[first_list_pointer] == second_List[second_list_pointer]:
                counter += 1
                first_list_pointer += 1
                second_list_pointer += 1
            elif first_list[first_list_pointer] < second_List[second_list_pointer]:
                first_list_pointer += 1
            else:
                second_list_pointer += 1
        else:
            break
    return counter


print(get_answer(first_list, second_List))
print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"Memory usage: {memory_info.rss / 1024 / 1024} MB")
