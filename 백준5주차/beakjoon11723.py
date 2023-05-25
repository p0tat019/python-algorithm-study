import sys

S = [False] * 21

M = int(sys.stdin.readline())

for _ in range(M):
    calcul = sys.stdin.readline().split()
    cal = calcul[0]

    if cal == "add":
        x = int(calcul[1])
        S[x] = True
    elif cal == "remove":
        x = int(calcul[1])
        S[x] = False
    elif cal == "check":
        x = int(calcul[1])
        if S[x] == True:
            print('1')
        else:
            print('0')
    elif cal == "toggle":
        x = int(calcul[1])
        S[x] = not S[x]
    elif cal == "all":
        S = [True] * 21
    elif cal == "empty":
        S = [False] * 21
