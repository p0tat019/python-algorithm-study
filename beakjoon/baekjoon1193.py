# 1/1 -> 1/2,2/1 -> 3/1,2/2,1/3 -> 1/4,2/3,3/2,4/1 -> ... 순서로 배열

x = int(input())
i = 1 # 몇번 째 줄인지 확인
while x > i:
    x -= i
    i += 1
    
if i%2 == 0:
    a=x
    b=i-x+1
else:
    a=i-x+1
    b=x
print(a, "/", b, end ="")


