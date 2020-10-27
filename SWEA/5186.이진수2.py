t = int(input())
for tc in range(1, t+1):
    num = float(input())
    result = ''
    for i in range(12):
        num *= 2
        result += str(int(num) % 2)
        if num % 1 == 0:
            break
    else:
        result = 'overflow'
    print('#{} {}'.format(tc, result))
