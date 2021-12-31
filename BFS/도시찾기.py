from collections import deque

n, m, k, x = map(int, input().split()) # 도시의 갯수, 도로의 갯수, 거리정보, 출발도시 번호를 입력
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split()) # 도시의 정보 입력받기
    graph[a].append(b)

dist = [-1] * (n+1) # 모든 도시에 대한 최단 거리를 초기화
dist[x] = 0 # 출발도시의 거리는 0으로 설정

# bfs 수행
queue = deque([x])
while queue: # 비어있을 때까지 반복
    city = queue.popleft()

    for n_city in graph[city]: # 모든 도시를 확인하면서
        if dist[n_city] == -1: # 방문을 하지 않았다면
            dist[n_city] = dist[city] + 1 # 최단거리를 갱신
            queue.append(n_city)

check = False

for i in range(n+1): # 도시의 개수를 확인하면서
    if dist[i] == k: # 최단거리가 k가 되면
        print(i)
        check = True

if check == False:
    print(-1)

