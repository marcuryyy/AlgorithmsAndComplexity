import time
from memory_profiler import memory_usage
m_start = memory_usage()[0]

def find_composable_strings(strings):
    composable_strings = set()
    string_set = set(strings)

    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if strings[i] + strings[j] in string_set:
                composable_strings.add(strings[i] + strings[j])
            elif strings[j] + strings[i] in string_set:
                composable_strings.add(strings[j] + strings[i])
            elif strings[i] * 2 in string_set:
                composable_strings.add(strings[i] * 2)
            elif strings[j] * 2 in string_set:
                composable_strings.add(strings[j] * 2)

    return list(composable_strings)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


with open('input.txt') as f:
    n = int(f.readline())
    strings = [f.readline().strip('\n') for _ in range(n)]
    now = time.perf_counter()
    composable_strings = merge_sort(find_composable_strings(strings))
    for string in composable_strings:
        print(string)
    print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
    print(f"{memory_usage()[0] - m_start} Mb")
