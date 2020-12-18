for _ in range(10):
    num = input()
    if num == '0':
        break
    num = num[::-1]
    s = 0

    for i in num:
        s += int(i)
    print(num, s)

num = input()
