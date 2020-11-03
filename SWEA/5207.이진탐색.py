import sys
sys.stdin = open('input.txt', 'r')

def f():
    rs = 0
    for b in B:
        before = 0
        l = 0
        r = n - 1
        while l<=r:
            m = (l+r)//2
            if b == A[m]:
                rs += 1
                break
            elif b<A[m]:
                r = m-1
                curr = 1
            elif b>A[m]:
                l = m+1
                curr = 2
            if before == curr:
                break

            before = curr
    return rs


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    print('#{} {}'.format(tc, f()))
