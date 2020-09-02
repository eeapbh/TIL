import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    # k:충전으로 이동가능 횟수
    # m:충전소 갯수
    # n:정류장갯수
    k, n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    bus = [0]*(n+1)
    for i in range(n+1):
        for number in numbers:
            if i == number:
                bus[i] = 1

    cnt = 0 # 충전소 들리는 횟수
    x = 0 # 현재위치
    nx = 0
    while 1:
        x += k
        if x>=n:
            break

        if bus[x] == 1:
            cnt += 1

        else:
            check = 0
            for j in range(1, k):

                nx = x-j
                if bus[nx] == 1:
                    x = nx
                    cnt += 1
                    break
                else:
                    check += 1
            if check == k-1:
                cnt = 0
                break


    print('#{} {}'.format(tc, cnt))
