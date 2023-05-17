import sys

N, L = map(int, input().split())  # 숫자 개수와 테이프 길이 받기
x = list(map(int, input().split()))  # 위치값 받기
x.sort()  # 오름차순 정렬

tape = 0
start = x[0]
for i in x:
    if i <= start + L - 1:  # 현재 위치가 테이프로 막힌 범위에 속하는 경우
        continue
    else:  # 테이프로 막힌 범위를 넘어선 경우
        tape += 1
        start = i

tape += 1  # 마지막 위치에 테이프가 더 필요하므로 1을 추가

print(tape)
