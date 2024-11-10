import time
from memory_profiler import memory_usage
m_start = memory_usage()[0]
now = time.perf_counter()
with open('input.txt') as f:
    V, M = map(int, f.readline().split())
    numbers = [int(f.readline()) for _ in range(V)]

    tree = [0] * (2 * V)

    for i in range(V):
        tree[V + i] = numbers[i]
    for i in range(V - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]


    def updateTree(index, value):
        tree[index + V] = value
        index += V
        i = index
        while i > 1:
            tree[i // 2] = tree[i] + tree[i ^ 1]
            i = i // 2

    def queryTree(l, r):
        sum = 0
        l += V
        r += V
        while l < r:
            if (l & 1) > 0:
                sum += tree[l]
                l += 1
            if (r & 1) > 0:
                r -= 1
                sum += tree[r]
            l = l // 2
            r = r // 2
        return sum

    for _ in range(M):
        code, n1, n2 = map(int, f.readline().split())
        if code == 1:
            L = n1
            R = n2
            sum_result = queryTree(L, R + 1)
            print(sum_result)
        elif code == 2:
            index = n1
            new_value = n2
            updateTree(index, new_value)
            numbers[index] = new_value
    print(f"Затраченное время: {round(time.perf_counter() - now, 2)} секунд")
    print(f"{memory_usage()[0] - m_start} Mb")
