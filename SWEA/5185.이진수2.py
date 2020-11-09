import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n, number = input().split()
    n = int(n)
    number = int(number, 16)
    number = format(number, 'b')
    if len(number) != n*4:
        number = '0'*  ((n*4)-len(number)) + number
    print('#{} {}'.format(tc, number))