import sys

# DFS 메서드 정의
def dfs(graph, node, visited):
    # 해당 노드를 방문 처리
    visited[node] = True
    # 한 노드로부터 인접한 다른 노드를 재귀적으로 방문 처리
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)

N = int(input())  # 컴퓨터 수 받기
pair = int(input())  # 컴퓨터 쌍 받기

# 인접 리스트 생성
graph = []
for _ in range(N + 1):
    line = []
    graph.append(line)

for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 노드별로 방문 정보를 리스트로 표현
visited = [False] * (N + 1)  # 방문 리스트 크기를 N+1로 설정

# 정의한 DFS 메서드 호출 (노드 1을 탐색 시작 노드로 설정)
dfs(graph, 1, visited)

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 출력
count = sum(visited) - 1  # 방문한 컴퓨터 수에서 1번 컴퓨터 제외
print(count)
