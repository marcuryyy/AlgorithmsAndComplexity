N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

temp_city = [[float('inf') for _ in range(M)] for _ in range(N)]
temp_city[0][0] = 0

for i in range(1, M):
    energy_cost = max(0, city[0][i] - city[0][i-1])
    temp_city[0][i] = temp_city[0][i-1] + energy_cost


for j in range(1, N):
    energy_cost = max(0, city[j][0] - city[j-1][0])
    temp_city[j][0] = temp_city[j-1][0] + energy_cost

for i in range(1, N):
    for j in range(1, M):
        energy_from_top = max(0, city[i][j] - city[i-1][j])
        energy_from_left = max(0, city[i][j] - city[i][j-1])

        temp_city[i][j] = min(temp_city[i-1][j] + energy_from_top, temp_city[i][j-1] + energy_from_left)


print(temp_city[N-1][M-1])
