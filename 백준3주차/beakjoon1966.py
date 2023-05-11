from collections import deque
import sys

testcase = int(sys.stdin.readline())

for i in range(testcase):
    a, b = map(int, sys.stdin.readline().split())
    g = deque(map(int, sys.stdin.readline().split()))
    cnt = 0
    while g:
        best = max(g)
        first = g.popleft()
        m  -= 1

        if best == first:
          cnt += 1
          if m < 0:
            print(cnt)
            break
        else:
            g.append(first)
            if m < 0:
              m = len(g) - 1  
