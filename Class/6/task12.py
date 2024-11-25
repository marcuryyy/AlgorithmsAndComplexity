n = int(input())
scores = list(map(int, input().split()))
bag_weight = sum(scores) // 2

A = [[0 for _ in range(bag_weight + 1)] for _ in range(n + 1)]

for k in range(1, n + 1):
    for s in range(bag_weight + 1):
        if scores[k - 1] > s:
            A[k][s] = A[k - 1][s]
        else:
            A[k][s] = max(A[k - 1][s], A[k - 1][s - scores[k - 1]] + scores[k - 1])

if sum(scores) / 2 == A[n][bag_weight]:
    print("True")
else:
    print("False")
