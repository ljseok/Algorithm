from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input()))) # 2차원 리스트 입력받기
# 상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y): # bfs함수 정의
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft() #

        for i in range(4): # 4방향으로 위치확인
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 범위를 벗어난다면 무시
                continue
            if graph[nx][ny] == 0: # 벽인경우 무시
                continue
            if graph[nx][ny] == 1: # 노드를 처음 방문하는 경우에만 최단거리를 계산
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1] # 최단거리 반환
print(bfs(0,0))