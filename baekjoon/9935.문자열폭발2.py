import sys
sys.stdin = open('input.txt', 'r')

line = input()
boom = input()

tmp = []

for i in line:
    tmp.append(i)
    if len(tmp) >= len(boom):
        ans = 1
        for j in range(-1, (-len(boom))-1, -1):
            if tmp[j] != boom[j]:
                ans = 0
                break
        if ans:
            for _ in range(len(boom)):
                tmp.pop()

if len(tmp) == 0:
    print('FRULA')
else:
    print(''.join(tmp))

