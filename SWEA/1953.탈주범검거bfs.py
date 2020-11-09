import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
def bfs(x, y, cnt):

    q = []
    q.append((x, y, cnt))
    visit.append((x, y))
    while q:
        cx, cy, ccnt = q.pop(0)
        # visit.append((cx, cy))
        v = arr[cx][cy]
        if v:
            for a, b in delta[v]:
                nx = cx+a
                ny = cy+b
                if 0<=nx<n and 0<=ny<m and (nx, ny) not in visit and ccnt<l:
                    if (a, b) == (-1, 0):  # 상일떄는 다음께 1, 2, 5, 6일때만가능
                        if arr[nx][ny] in [1, 2, 5, 6]:
                            q.append((nx, ny, ccnt+1))
                            visit.append((nx, ny))
                    elif (a, b) == (1, 0):  # 하일떄는 다음께 1, 2, 4, 7
                        if arr[nx][ny] in [1, 2, 4, 7]:
                            q.append((nx, ny, ccnt+1))
                            visit.append((nx, ny))
                    elif (a, b) == (0, -1):  # 좌일떄는 다음께 1, 3, 4, 5
                        if arr[nx][ny] in [1, 3, 4, 5]:
                            q.append((nx, ny, ccnt+1))
                            visit.append((nx, ny))
                    else:  # 우일떄는 다음께 1, 3, 6, 7
                        if arr[nx][ny] in [1, 3, 6, 7]:
                            q.append((nx, ny, ccnt+1))
                            visit.append((nx, ny))

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
    bfs(r, c, 1)
    # print(visit)
    print('#{} {}'.format(tc, len(visit)))