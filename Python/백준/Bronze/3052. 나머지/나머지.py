# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

num = []

for _ in range(10):
    num.append(int(input()))

for i in range(len(num)):
    num[i] = num[i] % 42
    
num = list(set(num))
print(len(num))