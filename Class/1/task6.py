N, M, MOD = map(int, input().split())


def get_answer(N: int, M: int, MOD: int):
    list_a_i: list[int] = [0 for _ in range(N + 1)]
    list_x_i: list[int] = [0 for _ in range(M)]
    total_sum: int = 0

    for i in range(N, -1, -1):
        list_a_i[i] = int(input())

    for i in range(M):
        list_x_i[i] = int(input())

    list_a_length: int = len(list_a_i)

    for x in list_x_i:
        total_sum = 0
        for i in range(list_a_length):
            total_sum += list_a_i[i] * (x ** i)

    return total_sum % MOD
