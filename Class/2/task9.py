from memory_profiler import memory_usage
import time

m_start = memory_usage()[0]
now = time.perf_counter()


def process_file(input_path):
    answer = []

    with open(input_path) as f:
        n = int(f.readline())

        for i in range(n):
            count_sort_lst = [[] for _ in range(10_001)]
            lst = []
            temp = list(map(int, f.readline().split()))[1:]
            for i in range(0, len(temp)-1, 2):
                count_sort_lst[temp[i]].append([temp[i], temp[i +1]])

            for j in range(10_001):
                if len(count_sort_lst[j]) > 1:
                    for k in range(len(count_sort_lst[j])):
                        lst.append(count_sort_lst[j][k])
                elif count_sort_lst[j]:
                    lst.append(count_sort_lst[j])
            answer.append(solve(lst))

    return "\n".join(str(answer[i]) for i in range(n))


def solve(lst):
    guards_at_time = [0] * 10001
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            guards_at_time[lst[i][j][0]] += 1
            guards_at_time[lst[i][j][1]] -= 1

    count = 0

    alone_guards = 0
    min_guards_at_time = float('inf')
    prev_count = 0

    for j in range(10000):
        count += guards_at_time[j]
        min_guards_at_time = min(count, min_guards_at_time)
        if count == 1 and prev_count != 1:
            alone_guards += 1
        prev_count = count

    if min_guards_at_time != 1:
        return "Wrong Answer"

    if alone_guards != len(lst):
        return "Wrong Answer"

    return "Accepted"


print(process_file('input.txt'))
print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
print(f"{memory_usage()[0] - m_start} Mb")
