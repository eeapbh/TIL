def convert(n, base):
    T = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
while 1:
    info = input().split()
    if info[0] == 0:
        break
    a = info[0]
    n = info[1]
    b = info[2]
    num = int(n, int(a))
    print(convert(num, int(b)))
