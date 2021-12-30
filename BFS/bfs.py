from collections import deque # deque 라이브러리 사용

def bfs(graoh, start, visited): # bfs 함수 정의
    queue = deque([start])
    visited[start] = True # 현재노드를 방문처리

    while queue: # 큐가 빌때까지 반복
        v = queue.popleft() # 큐에서 하나의 원소를 뽑는디.
        print(v, end=' ')

        for i in graoh[v]:
            if not visited[i]: # 방문하지 않았다면
                queue.append(i) # 원소 삽입
                visited[i] = True

graph = [[],[2,3,8,],[1,7],[1,4,5],[3,5,],[3,4],[7],[2,6,8],[1,7]]

visited = [False] * 9

bfs(graph, 1, visited)