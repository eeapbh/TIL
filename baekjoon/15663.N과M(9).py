import sys
sys.stdin = open('input.txt', 'r')

# def perm(idx):
#     if idx == m:
#         tmp = sel[:]
#
#         total.append(tmp)
#         return
#
#     for i in range(n):
#         if not visited[i]:
#             sel[idx] = arr[i]
#             visited[i] = 1
#             if sel in total:
#                 visited[i] = 0
#                 continue
#             perm(idx+1)
#             visited[i] = 0
#
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# sel = [0]*m
# visited = [0]*n
# total = []
#
# perm(0)
# for t in total:
#     print(*t)

def perm(idx):
    if idx == m:
        total.add(tuple(sel))
        return

    for i in range(n):
        if not visited[i]:
            sel[idx] = arr[i]
            visited[i] = 1

            perm(idx+1)
            visited[i] = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
sel = [0]*m
visited = [0]*n
total = set()

perm(0)
b = sorted(total)
for t in b:
    print(*t)