import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
def DFS(x, y, cnt):
    visit.append((x, y))
    if cnt == l:
        return
    v = arr[x][y]
    if v:
        for a, b in delta[v]:
            nx = x+a
            ny = y+b
            if 0<=nx<n and 0<=ny<m and (nx, ny) not in visit:
                if (a, b) == (-1, 0): # 상일떄는 다음께 1, 2, 5, 6일때만가능
                    if arr[nx][ny] in [1, 2, 5, 6]:
                        DFS(nx, ny, cnt+1)
                elif (a, b) == (1, 0): # 하일떄는 다음께 1, 2, 4, 7
                    if arr[nx][ny] in [1, 2, 4, 7]:
                        DFS(nx, ny, cnt+1)
                elif (a, b) == (0, -1): # 좌일떄는 다음께 1, 3, 4, 5
                    if arr[nx][ny] in [1, 3, 4, 5]:
                        DFS(nx, ny, cnt+1)
                else: # 우일떄는 다음께 1, 3, 6, 7
                    if arr[nx][ny] in [1, 3, 6, 7]:
                        DFS(nx, ny, cnt+1)

for tc in range(1, t+1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = []
    delta = [[(0, 0)],
        [(-1, 0), (1, 0), (0, -1), (0, 1)],
             [(-1, 0), (1, 0)],
             [(0, -1), (0, 1)],
             [(-1, 0),(0, 1)],
             [(1, 0), (0, 1)],
             [(1, 0), (0, -1)],
             [(-1, 0), (0, -1)]
             ]
    DFS(r, c, 1)
    print('#{} {}'.format(tc, len(visit)))