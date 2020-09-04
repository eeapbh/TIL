import sys
sys.stdin = open('input.txt', 'r')

def BFS(start):
    visit[start] = 1
    queue = []
    queue.append(start)
    while len(queue) > 0:
        curr = queue.pop(0)
        for i in arr[curr]:
            if not visit[i]:
                visit[i] = 1
                queue.append(i)
                visit[i] = visit[curr]+1
            if i == g:
                return visit[i]-1
    return 0


t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    arr = [[0] for i in range(v+1)]
    visit = [0] * (v+1)
    for _ in range(e):
        i, j = map(int, input().split())
        arr[i].append(j)
        arr[j].append(i)
    s, g = map(int, input().split())
    print('#{} {}'.format(tc, BFS(s)))