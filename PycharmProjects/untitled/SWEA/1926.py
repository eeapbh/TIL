n = int(input())
numbers = []
for i in range(1, n+1):
    numbers.append(str(i))
for j in numbers:
    count = 0
    for k in j[::-1]:
        if k in {'3', '6', '9'}:
            print('-', end = '')
            count +=1
    if count <=0:
        print(j, end = '')
    print(' ', end='')

