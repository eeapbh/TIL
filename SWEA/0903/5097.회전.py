t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    number = list(map(int, input().split()))
    print('#{} {}'.format(tc, number[m%n]))
