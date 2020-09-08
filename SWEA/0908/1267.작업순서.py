def BFS(x):
    queue = []
    queue.append(x)
    visited[x] = 1

    while len(queue)>0:
        curr = queue.pop(0)
        result.append(curr)
        for i in range(1, v+1):
            if arr[curr][i] == 1 and visited[i] == 0:
                if visit[i] == 1:
                    queue.append(i)
                    visited[i] = 1
                else:
                    visit[i] -= 1



for tc in range(1, 11):
    v, e = map(int, input().split())
    arr = [[0]*(v+1) for _ in range(v+1)]
    visit = [0]*(v+1)
    visited = [0]*(v+1)
    result = []
    data = list(map(int, input().split()))
    for i in range(0, 2*e, 2):
        arr[data[i]][data[i+1]] = 1
        visit[data[i+1]] += 1

    for f in range(1, len(visit)):
        if visit[f] == 0:
            BFS(f)

    print('#{}'.format(tc), end=' ')
    for r in result:
        print(r, end=' ')
    print()

