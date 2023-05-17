import sys

input = sys.stdin.readline

N = input().rstrip()  # 방 번호 입력받기, 개행문자 제거

num_sets = [0] * 10  # 각 숫자의 개수를 저장할 리스트

for i in N:
    num = int(i)
    if num == 6 or num == 9:
        # 6이나 9는 한 세트로 사용 가능하므로 둘 중 하나에 할당
        # 더 작은 곳에 넣는 이유는 예를 들면 6669일경우 6이 3개이지만
        # 2세트에서 위 수열을 나타낼 수 있기 때문에 작은 수에 넣으면 해결
        if num_sets[6] <= num_sets[9]:
            num_sets[6] += 1
        else:
            num_sets[9] += 1
    else:
        num_sets[num] += 1

# 필요한 세트의 개수의 최댓값이 필요한 세트의 최소 개수가 됨
min_sets = max(num_sets)

print(min_sets)
