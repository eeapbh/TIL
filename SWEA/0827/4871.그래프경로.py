def DFS(x):
    visted[x] = 1
    for i in range(1, len(arr)):
        if arr[x][i] == 1:
            DFS(i)

t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    arr = [[0]*(v+1) for _ in range(v+1)]
    visted = [0]*(v+1)

    for i in range(e):
        st, ed = map(int, input().split())
        arr[st][ed] = 1

    S, G = map(int, input().split())
    DFS(S)

    if visted[G] == 1:
        print('#{} 1'.format(tc))
    if visted[G] == 0:
        print('#{} 0'.format(tc))


