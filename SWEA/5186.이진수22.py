import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    number = float(input())
    ans = ''
    while 1:
        number = number*2
        ans += str(int(number))
        number = number-int(number)

        if len(ans) > 12:
            ans = 'overflow'
            break
        if number == 0:
            break

    print('#{} {}'.format(tc, ans))



