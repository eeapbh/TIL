import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
#
# n = int(input())
# arr = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     tmp = list(map(int, input().split()))
#     arr[tmp[0]].append([tmp[1], tmp[2]])
#     arr[tmp[1]].append([tmp[0], tmp[2]])
# result1 = [0 for _ in range(n+1)]
#
# def dfs(start, arr, result):
#     for line in arr[start]:
#         if len(line) == 0:
#             break
#         else:
#             e = line[0]
#             d = line[1]
#             if result[e] == 0:
#                 result[e] = result[start] + d
#                 dfs(e, arr, result)
#
# dfs(1, arr, result1)
# result1[1] = 0
#
# long = 0
# idx = 0
# for i in range(len(result1)):
#     if result1[i] > long:
#         long = result1[i]
#         idx = i
#
# result2 = [0 for _ in range(n+1)]
# dfs(idx, arr, result2)
#
# result2[idx] = 0
# print(max(result2))
def bfs(x, mode):
    q = deque()
    q.append(x)
    result = [0 for _ in range(n+1)]
    while q:
        s = q.popleft()
        for e, d in arr[s]:
            if result[e] == 0:
                result[e] = result[s] + d
                q.append(e)
    if mode == 1:
        return result.index(max(result))
    else:
        return max(result)


n = int(input())
arr = [[] for _ in range(n+1)]
for i in range(n-1):
    s, e, d = map(int, input().split())
    arr[s].append([e, d])
    arr[e].append([s, d])

print(bfs(bfs(1, 1), 2))

