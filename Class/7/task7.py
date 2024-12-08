class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))


def bellman_ford(G: Graph, weights, s):
    d = {v: float('inf') for v in G.adjacency_list.keys()}
    pi = {v: None for v in G.adjacency_list.keys()}
    d[s] = 0

    num_vertices = len(G.adjacency_list)

    for _ in range(num_vertices - 1):
        for u in G.adjacency_list:
            for v, weight in G.adjacency_list[u]:
                if d[v] > d[u] + weights[(u, v)]:
                    d[v] = d[u] + weights[(u, v)]
                    pi[v] = u

    for u in G.adjacency_list:
        for v, weight in G.adjacency_list[u]:
            if d[v] > d[u] + weights[(u, v)]:
                return None, None

    return d, pi


N, M, S = map(int, input().split())

graph = Graph()

weights = {}

for _ in range(M):
    si, ei, wi = map(int, input().split())
    graph.add_edge(si, ei, wi)

for u in graph.adjacency_list:
    for v, weight in graph.adjacency_list[u]:
        weights[(u, v)] = weight

d, pi = bellman_ford(graph, weights, S)

if d is None:
    print("IMPOSSIBLE")
else:
    answer_str = ''
    for answer in d.values():
        if isinstance(answer, int):
            answer_str += str(answer) + ' '
        else:
            answer_str += "UNREACHABLE"
    print(answer_str.strip())
