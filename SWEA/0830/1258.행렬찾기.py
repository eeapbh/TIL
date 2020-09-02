# # import sys
# # sys.stdin = open('input.txt', 'r')
#
#
# # 0이 아닌곳에서 dfs탐색하면서 좌표들 저장
# def DFS(x, y):
#
#     visited.append((x, y))
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0<=nx<n and 0<=ny<n:
#             if not (nx, ny) in visited and arr[nx][ny] != 0:
#                 DFS(nx, ny)
# #탐색한 좌표들 다 0으로 바꿔줌
# def make_zero(x, y):
#     for i in range(c):
#         for j in range(r):
#             arr[x+i][y+j] = 0
#
#
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     save = []
#     visited = []
#     print('#{}'.format(tc), end=' ')
#
#     for i in range(n):
#         for j in range(n):
#             a = b = c = r = 0
#             if arr[i][j] != 0: # 0이 아니면 탐색시작
#                 DFS(i, j)   #다돌면서 좌표저장함
#                 visited.sort(key=lambda x:(x[0], x[1]))# 좌표들 열행 오름차순으로 정렬
#                 c = visited[-1][0]- visited[0][0]+1 # 젤큰거에서 작은거 빼서 길이구함
#                 r = visited[-1][1]- visited[0][1]+1
#                 save.append((c, r)) # 세로 가로 길이구함
#                 make_zero(i, j) # 탐색한곳 0으로 바꿈
#                 visited = []
#
#     save.sort(key=lambda x:(x[0]*x[1], x[0])) # 가로세로모은 리스트를 크기순그다음 세로길이순으로 정렬
#     print(len(save), end = ' ')
#     for s in save:
#         print(s[0], s[1], end = ' ')
#     print()


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    save = []
    for i in range(n):
        for j in range(n):
            r = c = 0
            for a in range(i, n):
                if arr[a][j]:
                    r += 1
                else:
                    break
            for b in range(j, n):
                if arr[i][b]:
                    c += 1
                else:
                    break
            if r>=1 or c>=1:
                save.append((r,c))
                for x in range(r):
                    for y in range(c):
                        arr[i+x][j+y] = 0

    save.sort(key=lambda x:(x[0]*x[1], x[0]))
    print('#{} {}'.format(tc, len(save)), end = ' ')
    for x, y in save:
        print(x, y, end =' ')
    print()

