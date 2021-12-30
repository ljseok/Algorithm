from itertools import permutations
from itertools import combinations
import heapq

'''
score = int(input())
if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
else:
    print("어머 !!!! 공부를 안하셨나요 ??? 어떻게 점수가 70점 아래일수가 있죠 ")
    print("당신의 학점은 기대도 하지 마세요 "
i = 1
result = 0

while i<=9:
    result += i
    i += 1
print(result)

result = 0

for i in range(1,100):
    result += i
    i += 1
print(result)

def add(a,b):
    return a+b
print("덧셈 연산 수행후 결과:", add(3,100))

def sub(a,b):
    return a-b
print("뺄셈 연산 수행후 결과:", sub(100,86))

def multi(a,b):
    return a*b
print("곱셈 연산 수행후 결과:", multi(3,100))

def divide(a,b):
    return a/b
print("나눗셈 연산 수행후 결과:", divide(100,50))

def mod(a,b):
    return a%b
print("나머지 연산 수행후  결과:", mod(100,3))

result = sum([1,2,3,4,5])
print(result)

result = min(7,8,6,5)
print(result)

result = max(1,10)
print(result)

result = eval("(3+5)*7")
print(result)

data = sorted([9,1,8,2,4], reverse=True)
print(data)

data = [2,3,5,6,9,5,2,10,3]
data.sort(reverse=True)
print(data)

data = ['A','B','C','D','E','F']
result = list(combinations(data,3))
print(result)

def heapsort(iterable):
    h = []
    result = []

    for a in iterable:
        heapq.heappush(h,-a)

    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([13,5,7,9,2,4,6,8,0])
print(result)
'''

lol = [[1,2,3],[4,5,],[6,7,8,9]]
print(lol[0])
print(lol[2][1])
for sub in lol:
    for item in sub:
        print(item, end=' ')
    print()