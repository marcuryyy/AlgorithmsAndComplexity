N = int(input())

coordinates = [list(map(int, input().split())) for _ in range(N)]

max_dist = 0

G = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N-1):
    for j in range(N):
        G[i][j] = ((coordinates[j][0] - coordinates[i][0])**2 + (coordinates[i][1] - coordinates[j][1])**2) ** 0.5

visited = {0}
weights = []


while len(visited) != N:
    min_length = float('inf')
    index = 0
    for node in visited:
        for i in range(N):
            if G[node][i] < min_length and G[node][i] != 0 and i not in visited:
                min_length = G[node][i]
                index = (node, i, )
    visited.add(index[1])
    weights.append(G[index[0]][index[1]])

print(round(max(weights), 4))
