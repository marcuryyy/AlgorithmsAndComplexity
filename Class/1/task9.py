def get_permutations_amount(N, M):
    if M == 0:
        return 1
    if M == 1:
        return N
    if N < M:
        return 0

    total_permutations = 0
    for distance in range(N):
        if distance == 0:
            if M < (N / 2):
                total_permutations += N // (M - 1) - 1
            else:
                total_permutations += N // (M - 1) + 1
        else:
            formula = ((N - distance) // (M - 1)) - 1
            total_permutations += formula if formula > 0 else 0

    open("output.txt", "w").write(str(total_permutations))


N, M = map(int, open("input.txt").readline().split())
