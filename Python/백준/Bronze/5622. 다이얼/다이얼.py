# 아스키 코드를 이용하는 풀이는 생각하지 못 했는데 앞으로 참고할 것.
dial = "22233344455566677778889999"

word = input()
sec = 0
for i in word:
    index = ord(i) - ord('A') 
    n = int(dial[index])   
    sec += n+1 # 이런 방식도 앞으로 참고
print(sec)