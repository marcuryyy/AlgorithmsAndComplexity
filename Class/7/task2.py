def is_optimal_map(n):
    r_graph = {i: [] for i in range(1, n + 1)}
    b_graph = {i: [] for i in range(1, n + 1)}

    for i in range(1, n):
        routes = input()
        for dest, road in enumerate(reversed(routes)):
            if road == 'R':
                r_graph[i].append(n - dest)
            else:
                b_graph[i].append(n - dest)

    def dfs(graph, start, end, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        if start == end:
            return True
        for neighbor in graph.get(start):
            if neighbor not in visited:
                if dfs(graph, neighbor, end, visited):
                    return True
        return False

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if dfs(r_graph, i, j) and dfs(b_graph, i, j):
                return False

    return True


result = is_optimal_map(int(input()))
print("YES") if result else print("NO")

