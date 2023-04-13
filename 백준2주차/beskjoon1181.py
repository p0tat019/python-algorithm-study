N = int(input())
a = []
for _ in range(N):
    string = input()
    a.append(string)

a_set = set(a) #중복제거
lst_a = list(a_set)# 리스트로 변환 뒤 길이별 정렬
lst_a.sort()
lst_a.sort(key = len)

for i in lst_a:
    print(i)







