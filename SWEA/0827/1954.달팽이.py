t = int(input())
for tc in range(1, t+1):
    N = int(input())
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r  = c = 0
    i = 0
    num = 1
    arr = [[0] * N for _ in range(N)]
    while num <= N*N:

        arr[r][c] = num
        num += 1

        nr = r + dr[i]
        nc = c + dc[i]

        if 0<= nr < N and 0<= nc <N and arr[nr][nc] == 0:
           r, c = nr, nc
        else:
            i = (i+1)%4
            r += dr[i]
            c += dc[i]
    print('# {}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()

