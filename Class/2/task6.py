import time
from memory_profiler import memory_usage
# def calculate_sequence(N, K, M, L):
#     count_elems = [0 for _ in range(L)]
#     count_elems[K] += 1
#     prev_elem = K
#     for i in range(1, N):
#         Ai = (prev_elem * M) % (2 ** 32 - 1) % L
#         prev_elem = Ai
#         count_elems[Ai] += 1
#     sequence = do_sort(count_elems)
#     return sequence
#
#
# def sum_odd_elements(sequence, L):
#     odd_sum = 0
#     for i in range(0, len(sequence), 2):
#         odd_sum = (odd_sum + sequence[i])
#     return odd_sum % L
#
#
# def do_sort(lst: list[int]):
#     sequence = []
#     for i in range(len(lst)):
#         if lst[i] > 0:
#             temp_lst = [i] * lst[i]
#             sequence += temp_lst
#     return sequence
#
#
# N, K, M, L = map(int, input().split())
# now = time.perf_counter()
# sequence = calculate_sequence(N, K, M, L)
#
# result = sum_odd_elements(sequence, L)
#
# print(time.perf_counter() - now)
# print(result)



m_start = memory_usage()[0]
def calculate_sequence(N, K, M, L):
    count_elems = [0 for _ in range(L)]
    count_elems[K] += 1
    prev_elem = K
    for i in range(1, N):
        Ai = (prev_elem * M) % L
        prev_elem = Ai
        count_elems[Ai] += 1
    sequence = do_sort(count_elems)
    return sequence

def do_sort(lst: list[int]):
    odd_sum = 0
    elem_counts = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            elem_counts += lst[i]
            if elem_counts % 2 == 0 and elem_counts - (elem_counts - lst[i]) == 1:
                continue
            elif elem_counts % 2 != 0 and elem_counts - (elem_counts - lst[i]) == 1:
                odd_sum += i
            else:
                odd_sum += i * (elem_counts // 2 + elem_counts % 2)
    return odd_sum % L


N, K, M, L = map(int, input().split())
now = time.perf_counter()
sequence = calculate_sequence(N, K, M, L)

print(sequence)
print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"{memory_usage()[0] - m_start} Mb")
