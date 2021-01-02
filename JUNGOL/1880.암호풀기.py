import sys
sys.stdin = open('input.txt')
info = input()
line = input()
ans = ''
for i in line:
    if i == ' ':
        ans += i

    elif ord(i) >= 97:
        n = ord(i) - 97
        ans += info[n]
    else:
        n = ord(i) - 65
        tmp = ord(info[n]) -32
        ans += chr(tmp)
print('adf')