N = int(input()) #사람의 수
size_list = [] #빈 리스트 생성

for _ in range(N): 
    weight, height = map(int,input().split()) #몸무게와 키 값 받기
    size_list.append((weight, height)) # 몸무게와 키 리스트에 추가하기

for i in size_list:
    rank = 1
    for j in size_list:
        if i[0] > j[0] and i[1] > j[1]:
            rank += 1
    print(rank, end =" ")