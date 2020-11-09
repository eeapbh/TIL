import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    ans = 0
    while q:
        for a in range(len(q)):
            curr = q.popleft()
            if curr == m:
                return ans
            for i in (curr+1, curr-1, curr*2, curr-10):
                if 0<i<=1000000 and memo[i] == -1:
                    q.append(i)
                    memo[i] = 1

        ans += 1


def calc(num, idx):
    if idx == 0:
        return num+1
    elif idx == 1:
        return num-1
    elif idx == 2:
        return num*2
    else:
        return num-10

def bfs2():
    q = [0]*1000000
    front = rear = -1
    rear += 1
    q[rear] = (n, 0)
    memo[n] = 0
    while front != rear:
        front += 1
        cn, ccnt = q[front]
        if cn == m:
            return ccnt
        for i in range(4):
            next = calc(cn, i)
            if 0<next<=1000000 and memo[next] == -1:
                q[rear] = (next, ccnt+1)
                rear += 1
                memo[next] = memo[cn] + 1



t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    memo = [-1]* 1000001

    print('#{} {}'.format(tc, bfs()))