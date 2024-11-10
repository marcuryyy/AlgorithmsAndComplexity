import time
from memory_profiler import memory_usage
m_start = memory_usage()[0]
def check(pages, k, max_pages):
    current_pages = 0
    count_volumes = 1
    for i in range(len(pages)):
        if current_pages + pages[i] > max_pages:
            count_volumes += 1
            current_pages = 0
        current_pages += pages[i]
    return count_volumes <= k


def find(pages, k):
    left = max(pages)
    right = sum(pages)
    while left < right:
        mid = (left + right) // 2
        if check(pages, k, mid):
            right = mid
        else:
            left = mid + 1
    return left


with open("INPUT.TXT", "r") as f:
    n = int(f.readline())
    pages = list(map(int, f.readline().split()))
    k = int(f.readline())
    now = time.perf_counter()
    optimal_volume = find(pages, k)
    print(optimal_volume)
print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"{memory_usage()[0] - m_start} Mb")
