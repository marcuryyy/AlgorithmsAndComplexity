from decimal import Decimal
import time
from memory_profiler import memory_usage

m_start = memory_usage()[0]
n = 1000000

lst = [5 for _ in range(n)]
length = max(lst) + 1
now = time.perf_counter()

def do_sort(lst):
    length = max(lst) + 1
    temp_lst = [0] * (length)
    for company in lst:
        temp_lst[company] += 1
    sorted_companies = []
    for i in range(length):
        if temp_lst[i] > 0:
            for j in range(temp_lst[i]):
                sorted_companies.append(i)
    return sorted_companies


def calc(lst, l_p, r_p, counter):
    counter += Decimal(str((lst[l_p] + lst[r_p]))) * Decimal('0.01')
    temp = lst[l_p]
    lst[l_p] = 0
    lst[r_p] += temp
    l_p += 1
    r_p += 1
    return lst, counter, l_p, r_p


def solve(n, lst):
    prev_index = None
    can_solve = False
    counter = Decimal('0')
    lst = do_sort(lst)
    l_p = 0
    r_p = 1
    lst, counter, l_p, r_p = calc(lst, l_p, r_p, counter)
    n -= 1
    while n != 1:
        if r_p >= len(lst):
            r_p = l_p + 1
        if lst[l_p] == 0:
            if prev_index is not None:
                lst[l_p], lst[prev_index] = lst[prev_index], lst[l_p]
            l_p += 1
        if lst[r_p] == 0:
            r_p += 1
        elif lst[r_p] >= lst[l_p] or can_solve or n == 2:
            lst, counter, l_p, r_p = calc(lst, l_p, r_p, counter)
            n -= 1
            can_solve = False
            if prev_index is not None:
                l_p = prev_index
                prev_index = None
                r_p -= 1
        else:
            r_p += 1
            if r_p >= len(lst):
                can_solve = True
                r_p -= 1
            if lst[r_p] < lst[l_p]:
                if prev_index is None:
                    prev_index = l_p
                l_p += 1
            else:
                r_p -= 1
                can_solve = True

    return counter


print(solve(n, lst))
print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"{memory_usage()[0] - m_start} Mb")
