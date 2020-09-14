import sys
sys.stdin = open('input.txt', 'r')
def DFS(x):
    result.append(x)
    visit[x] = 1
    for i in range(1, n+1):
        if arr[x][i] == 1 and visit[i] == 0:
            DFS(i)


def BFS(x):
    q = []
    q.append(x)
    result2.append(x)
    while q:
        curr = q.pop(0)
        for i in range(1, n+1):
            if arr[curr][i] == 1 and i not in result2:
                result2.append(i)
                q.append(i)


n, m, v = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    st, ed = map(int, input().split())
    arr[st][ed] = arr[ed][st] =  1

visit = [0]*(n+1)
result = []
result2 = []
DFS(v)
BFS(v)
print(*result)
print(*result2)