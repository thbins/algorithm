# 바구니가 N개 (1번 ~ N번) -> 길이가 N인 배열을 이용
# 1 ~ N이 적힌 공이 여러 개 있다. 
# M번 공을 넣는다. -> M번 작업 수행
# 1번 공을 넣을 때마다 공을 넣을 범위를 정한다. (i번째부터 j번째까지)
# 정한 범위 안에는 k 번호의 공을 집어 넣는다. (1 <= k <= N)
# 바구니에 이미 공이 있으면 이전에 있던 공은 빼고 새로운 공을 넣는다.

N, M = map(int, input().split())
basket = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for c in range(i, j+1):
        basket[c-1] = k
        
print(*basket)    