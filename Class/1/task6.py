N, M, MOD = map(int, input().split())

list_a_i = [0 for _ in range(N + 1)]
list_x_i = [0 for _ in range(M)]

for i in range(N, -1, -1):
    list_a_i[i] = int(input())

for i in range(M):
    list_x_i[i] = int(input())

list_a_length = len(list_a_i)

for x in list_x_i:
    total_sum = 0
    for i in range(list_a_length):
        total_sum += list_a_i[i] * (x ** i)
    print(total_sum % MOD)



