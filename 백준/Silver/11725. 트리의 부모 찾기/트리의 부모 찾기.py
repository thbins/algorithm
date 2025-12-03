import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

# 1. 일단 간선 정보를 입력 받아서 인접 리스트로 만듬
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
parent = [0] * (N+1) # 여기에 부모 노드를 기록

def bfs(root):
    queue = deque([root])
    parent[root] = -1 # 루트는 부모 노드 없음
    
    while queue:
        cur = queue.popleft()
        
        for nxt in graph[cur]:
            if parent[nxt] == 0:
                parent[nxt] = cur # cur가 nxt의 부모 노드
                queue.append(nxt)
                
bfs(1)

for i in range(2, N+1):
    print(parent[i])