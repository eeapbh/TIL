import sys
sys.stdin = open('input.txt', 'r')

def BFS(x):
    q = []
    q.append(x)
    while q:
        curr = q.pop(0)
        for i in range(v+1):
            if arr[curr][i] == 1:
                q.append(i)
                if i in p:
                    return i
                else:
                    p.append(i)

def check(x):

    q = [x]
    count = 0
    while q:
        curr = q.pop(0)
        count += 1
        if len(arr2[curr]) == 2:
            q.append(arr2[curr][0])
            q.append(arr2[curr][1])
        if len(arr2[curr]) == 1:
            q.append(arr2[curr][0])
    return count
t = int(input())
for tc in range(1, t+1):
    v, e, s1, s2 = map(int, input().split())
    data = list(map(int, input().split()))

    arr = [[0]*(v+1) for _ in range(v+1)]

    arr2 = [[] for _ in range(v+1)]
    for i in range(e):
        arr[data[2*i+1]][data[2*i]] = 1
    for i in range(e):
        arr2[data[2*i]].append(data[2*i+1])
    p = []
    root = 0

    BFS(s1)
    root = BFS(s2)
    arr = []

    c = check(root)

    print('#{} {} {}'.format(tc, root, c))