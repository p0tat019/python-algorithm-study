from collections import deque
import sys

cnt = 0
result = deque()

a, b = map(int, sys.stdin.readline().split())
g = list(map(int, sys.stdin.readline().split()))

for i in range(a):
    result.append(i+1)

for j in range(b):
    result_len = len(result)
    result_index = result.index(g[j])
    if result_index < result_len - result_index:
        while True:
            if result[0] == g[j]:
                result.popleft()
                break
            else:
                k = result.popleft()
                result.append(k)
                cnt += 1

    else:
        while True:
            if result[0] == g[j]:
                result.popleft()
                break
            else:
                k = result.pop()
                result.appendleft(k)
                cnt += 1

print(cnt)
