import sys
sys.stdin = open('input.txt', 'r')

def BFS(start):
    queue = []
    queue.append(start)
    visited[start] = 1
    while len(queue) > 0:
        curr = queue.pop(0)
        for i in arr[curr]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                visited[i] += visited[curr]


for tc in range(1, 11):
    n, start = map(int, input().split())
    arr = [[0] for _ in range(101)]
    node = list(map(int, input().split()))
    for i in range(0, n, 2):
        arr[node[i]].append(node[i+1])
    visited = [0] * 101

    BFS(start)
    for i in range(100, -1, -1):
        if visited[i] == max(visited):
            print("#{} {}".format(tc, i))
            break




