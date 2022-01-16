def find_parent(parent,x): # 특정 원소가 속한 집합 찾기
    if parent[x] != x: # 부모노드가 아니라면
        parent[x] = find_parent(parent,parent[x]) # 부모노드를 찾을 떄 까지 재귀적으로 호출
    return parent[x]

def union_parent(parent,a,b): # 두개의 원소 합치기
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b: # a원소 보다 b원소 더 크다면
        parent[b] = a
    else: # b < a
        parent[a] = b

x,y = map(int,input().split()) # 노드의 갯수와 간선의 갯수 입력받기
parent = [0] * (x+1) # 부모테이블 초기화

for i in range(1,x+1): # 부모 테이블에서
    parent[i] = i # 부모를 자기자신으로 초기화

for i in range(y): # union 연산
    a,b = map(int,input().split())
    union_parent(parent,a,b)

print('각 원소가 속한 집합: ', end=' ')
for i in range(1, x+1):
    print(find_parent(parent,i), end=' ')
print()

print('부모 테이블: ', end=' ')
for i in range(1,x+1):
    print(parent[i], end=' ')
