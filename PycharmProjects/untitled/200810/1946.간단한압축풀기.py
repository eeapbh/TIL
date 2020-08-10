import sys
sys.stdin = open('input.txt', 'r')
t = int(input())

for tc in range(1, t+1):

    n = int(input())
    count = 0
    print(f'#{tc}')
    for i in range(n):
        s, num = map(str, input().split())

        for i in range(int(num)):
            print(s, end='')
            count += 1
            if count%10 ==0:
                print()
    print()

