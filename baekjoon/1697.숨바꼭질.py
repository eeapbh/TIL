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
            for i in (c+1, c-1, 2*c):
                if 0<=i<=100000 and memo[i] == -1:
                    q.append(i)
                    memo[i] = 1
        ans += 1

n, m = map(int, input().split())
memo = [-1]*100001
print(bfs())
