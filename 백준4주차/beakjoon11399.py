import sys

input = sys.stdin.readline
time = []
# 숫자 입력 받기
N = int(input())
# 사람당 쓰이는 시간 받기
p = list(map(int, sys.stdin.readline().split()))

# 시간 적은 순으로 배열
p.sort()

# 이전 사람시간과 자신의 시간을 더해 몇분을 기다렸는지 저장
for i in range(len(p)):
    time.append(sum(p[0:i+1]))
# 모든 사람이 기다린 시간 합
print(sum(time))
