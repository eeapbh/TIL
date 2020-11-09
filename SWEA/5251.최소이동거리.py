import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    dist[x] = 0
    while q:
        st = q.popleft()
        for i in arr[st]:
            ed = i[0]
            w = i[1]
            if dist[ed] == -1 or dist[ed] > dist[st] + w:
                dist[ed] = dist[st] + w
                q.append(ed)



t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v+1)]
    for i in range(e):
        st, ed, w = map(int, input().split())
        arr[st].append([ed, w])

    dist = [-1]*(v+1)
    bfs(0)
    print('#{} {}'.format(tc, dist[-1]))