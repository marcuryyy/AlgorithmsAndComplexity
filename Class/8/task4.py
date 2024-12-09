import time
from memory_profiler import memory_usage
import os

m_start = memory_usage()[0]


S = input()
now = time.perf_counter()
k, t = 0, 0
bin_l, bin_r = 1, len(S)


def hash_func(item, hash_size=10 ** 9):
    h = 0
    a = 3547
    b = 4985

    for i in range(len(item)):
        a = (a * b) % (hash_size - 1)
        h = (a * h + ord(item[i]) * (i + 1)) % hash_size

    return h


prev_l, prev_r = None, None

while bin_r - bin_l > 0 and bin_l < len(S) // 2 + 1:
    unique_hashes = set()
    counter = 0
    if bin_r == prev_r and bin_l == prev_l:
        if bin_r > bin_l:
            bin_r = mid
        else:
            bin_l = mid + 1
    mid = (bin_r + bin_l) // 2
    prev_r, prev_l = bin_r, bin_l
    if len(S) % mid == 0:
        for j in range(0, len(S) - mid + 1, mid):
            counter += 1
            if j == len(S) - mid:
                unique_hashes.add(hash_func(S[j:]))
            else:
                unique_hashes.add(hash_func(S[j:j + mid]))
        if len(unique_hashes) == 1:
            if counter > k and S[0:mid] * counter == S:
                k = counter
                t = S[0:mid]
                bin_r = mid
if k == t == 0:
    print(S)
else:
    print(t)

print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"{memory_usage()[0] - m_start} Mb")
