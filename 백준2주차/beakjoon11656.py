from collections import deque

a = deque()
string = input()
a.append(string)

for i in range(len(string)-1):
    a.append(a[0][i+1:])
    i += 1

b = sorted(a)

for j in range(len(b)):
    print(b[j])
    j += 1