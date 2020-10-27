import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [[] for _ in range(n+1)]

for _ in range(n):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)//2):
        arr[tmp[0]].append([tmp[2*i - 1], tmp[2*i]])
# print(arr)
result1 = [0 for _ in range(n+1)]

def DFS(start, arr, result):
    for e, d in arr[start]:
        if result[e] == 0:
            result[e] = result[start] +d
            DFS(e, arr, result)
DFS(1, arr, result1)
# print(result1)
result1[1] = 0
tpmax = 0
idx = 0
for i in range(len(result1)):
    if tpmax < result1[i]:
        tpmax = result1[i]
        idx = i

result2 = [0 for _ in range(n+1)]
DFS(idx, arr, result2)
# print(result2)
result2[idx] = 0
print(max(result2))