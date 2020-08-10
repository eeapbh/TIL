import sys
sys.stdin = open('input.txt', 'r')
t = int(input())

for tc in range(1, t+1):
    result = []
    n = int(input())
    number = list(map(int, input().split()))
    result = sorted(number)
    print(f'#{tc}', end = ' ')
    for r in result:
        print(r, end = ' ')
    print()