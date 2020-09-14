import sys
sys.stdin = open('input.txt', 'r')

def DFS(x):
    global cnt
    cnt += 1
    visit[x] = 1
    for i in range(1, v+1):
        if arr[x][i] == 1 and visit[i] == 0:
            DFS(i)

def find():
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if arr[i][j] == 1:
                return DFS(i)

v = int(input())
e = int(input())
arr = [[0]*(v+1) for _ in range(v+1)]
visit = [0]*(v+1)
for i in range(e):
    st, ed = map(int, input().split())
    arr[st][ed] = arr[ed][st] = 1
cnt = 0
find()
print(cnt-1)