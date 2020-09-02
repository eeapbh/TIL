t = int(input())
for tc in range(1, t+1):
    n = int(input())
    numbers = input()
    check = [0]*10

    for i in numbers:
        for j in range(10):
            if int(i) == j:
                check[j] += 1
    for i in range(9, -1, -1):
        if check[i] == max(check):
            print('#{} {} {}'.format(tc, i, check[i]))
            break