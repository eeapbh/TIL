import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    ans = 0
    while q:
        for _ in range(len(q)):
            c = q.popleft()
            if c == m:
                return ans
            for i in (c+1, c-1, c*2, c-10):
                if 1<=i<=1000000 and memo[i] == -1:
                    memo[i] = 1
                    q.append(i)
        ans += 1


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    memo = [-1]*1000001
    print('#{} {}'.format(tc, bfs()))
