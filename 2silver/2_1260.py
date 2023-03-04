from collections import deque

def make_graph(n, m):
    graph = [[] for _ in range(n+1)]  # 1부터 n까지의 노드를 갖는 그래프 생성
    for _ in range(m):
        u, v = map(int, input().split())  # 간선 정보 입력
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, n+1):
        graph[i].sort()  # 인접 리스트 정렬
    return graph

def dfs(graph, start):
    visited = [False] * len(graph)  # 방문 여부 체크 리스트
    stack = [start]  # 스택 초기화
    while stack:
        v = stack.pop()  # 스택에서 하나의 노드를 꺼내옴
        if not visited[v]:
            visited[v] = True  # 방문 처리
            print(v, end=' ')  # 해당 노드 출력
            stack += sorted(graph[v], reverse=True)  # 해당 노드와 연결된 노드들 스택에 추가

def bfs(graph, start):
    visited = [False] * len(graph)  # 방문 여부 체크 리스트
    queue = deque([start])  # 큐 초기화
    while queue:
        v = queue.popleft()  # 큐에서 하나의 노드를 꺼내옴
        if not visited[v]:
            visited[v] = True  # 방문 처리
            print(v, end=' ')  # 해당 노드 출력
            queue += sorted(graph[v])  # 해당 노드와 연결된 노드들 큐에 추가

n, m, start = map(int, input().split())
graph = make_graph(n, m)

dfs(graph, start)
print()
bfs(graph, start)