n, m = map(int, input().split())

def check(n, m):
    if m == 2:
        return format(n, 'b')
    elif m == 8:
        return format(n, 'o')
    elif m == 16:
        return format(n, 'x')
ans = check(n, m)
tmp = ''
for i in ans:
    if i not in '0123456789':
        i = chr(ord(i) - 32)
        tmp += i
    else:
        tmp += i
print(tmp)
