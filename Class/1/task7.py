import timeit

N = int(input())
weights = list(map(int, input().split()))


def get_min_diff(amount: int, rocks: list[int]):
    rocks = sorted(rocks)
    total_sum = 0
    prefix_sum = []
    heap_1_sum = 0
    heap_2_sum = 0
    for rock in rocks:
        total_sum += rock
        prefix_sum.append(total_sum)
    average = total_sum / amount
    for rock in rocks:
        if rock <= average:
            heap_1_sum += rock
        else:
            heap_2_sum += rock
    first_difference = abs(heap_1_sum - heap_2_sum)
    if amount > 2:
        second_difference = min(abs(prefix_sum[amount // 2] - (prefix_sum[-1] - prefix_sum[amount // 2])),
                                abs(prefix_sum[amount // 2 - 1] - (prefix_sum[-1] - prefix_sum[amount // 2 - 1])),
                                abs(prefix_sum[amount // 2 + 1] - (prefix_sum[-1] - prefix_sum[amount // 2 + 1])))
    else:
        second_difference = float('inf')
    answer = min(first_difference, second_difference)
    return answer


print(get_min_diff(N, weights))
