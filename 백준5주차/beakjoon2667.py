import sys
# 해결 못함 다시 시도
input = sys.stdin.readline
# DFS 메서드 정의
def dfs(graph, node, visited):
    # 해당 노드를 방문 처리
    visited[node] = True
    # 한 노드로부터 인접한 다른 노드를 재귀적으로 방문 처리
    for i in graph[node]:
        
        if not visited[i]:
            dfs(graph, i, visited)

graph = []

N = int(input())  # 지도의 크기 받기
for i in range(N):
    v = list(map,int(input().split()))
    graph.append(v)




# 노드별로 방문 정보를 리스트로 표현
visited = [False] * (N + 1)  # 방문 리스트 크기를 N+1로 설정

# 정의한 DFS 메서드 호출 (노드 1을 탐색 시작 노드로 설정)
dfs(graph, 1, visited)

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 출력
count = sum(visited) - 1  # 방문한 컴퓨터 수에서 1번 컴퓨터 제외
print(count)




def dfs(grid, row, col, visited):
    count = 1
    visited[row][col] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1 and not visited[new_row][new_col]:
            count += dfs(grid, new_row, new_col, visited)
    return count

def find_complexes(grid):
    n = len(grid)
    visited = [[False for _ in range(n)] for _ in range(n)]
    complexes = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                count = dfs(grid, i, j, visited)
                complexes.append(count)
    return complexes

# 지도를 입력받는다
n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().strip()))
    grid.append(row)

# 단지를 찾고, 단지 수와 각 단지에 속하는 집의 수를 계산한다
complexes = find_complexes(grid)
complexes.sort()

# 단지 수를 출력한다
print(len(complexes))
# 각 단지에 속하는 집의 수를 오름차순으로 출력한다
for count in complexes:
    print(count)
