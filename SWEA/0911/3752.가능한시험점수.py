import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))


    visit = [0] * (sum(arr)+1)
    q = [0]
    for a in arr:
        for i in range(len(q)):
            if visit[q[i]+ a]:
                continue
            visit[q[i] + a] = 1
            q.append(q[i]+ a)

    print('#{} {}'.format(tc, len(q)))