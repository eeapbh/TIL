# 인풋을 받는다
# 입력은 열 행 컬러
# 돌을 놓았을 때 8방향 탐색을 하면서 나와같은 컬러를 찾는다.
# (이때 중간에 공백이 있거나, 맵의 범위를 벗어나면 수행 x)
# 찾은 컬러의 좌표부터 지금 놓은 좌표까지 돌아오면서 샊깔을 모조리다 나의컬러로 바꾼다
# 위의 과정을 M번 반복하면 끝
# 11, 9, 7, 6, 12, 1, 3, 5
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    # 흑돌 = 1, 백돌 = 2
    arr = [[0]*n for _ in range(n)]

    arr[(n//2)-1][(n//2)-1] = 2
    arr[(n//2)-1][(n//2)] = 1
    arr[n//2][n//2] = 2
    arr[n//2][(n//2)-1] = 1

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, 1, -1, -1, 0, 1]

    for i in range(m):
        x, y, c = map(int, input().split())
        x, y = x-1, y-1

        for j in range(8):
            nx = x+dx[j]
            ny = y+dy[j]
            reverse = []
            while True:
                if 0>nx or 0>ny or n-1<nx or n-1<ny: #모서리 나가는 애들
                    reverse = []
                    break
                elif arr[nx][ny] == 0:
                    reverse = []
                    break
                elif arr[nx][ny] == c:

                    break
                else:
                    reverse.append((nx, ny))
                nx += dx[j]
                ny += dy[j]
            for a, b in reverse:
                arr[a][b] = c
        arr[x][y] = c
    cnt1 = cnt2 = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                cnt1 += 1
            elif arr[i][j] == 2:
                cnt2 += 1
    print('#{} {} {}'.format(tc, cnt1, cnt2))


