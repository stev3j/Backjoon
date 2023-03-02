N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N + 1)]
visited = [0]*(N + 1) # 방문 체크

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1 # 간선이 있는 곳에 1

def dfs(start):
    visited[start] = 1
    print(start, end=" ")

    for i in range(1, N+1):
        if visited[i] == 0 and graph[V][i] == 1:
            dfs(i)

def bfs(start):
    queue = [start]
    visited[start] = 0

    while queue:
        start = queue.pop(0)
        print(start, end=" ")
        for i in range(1, N+1):
            if visited[i] == 0 and graph[start][i] == 1:
                visited[i] = 0
                queue.append(i)

dfs(V)
print()
bfs(V)