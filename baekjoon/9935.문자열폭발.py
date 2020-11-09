import sys
sys.stdin = open('input.txt', 'r')

LINE = input()
BOOM = input()
line = list(LINE)
boom = list(BOOM)
n = len(line)
m = len(boom)
cnt = 0
while 1:
    if BOOM not in LINE:
        break

    for i in range(n-cnt):
        if line[i] == boom[0]:
            tmp = line[i:i+m]
            if tmp == boom:
                for j in range(i, i+m):
                    line[j] = '-1'
    cnt = 0
    for a in line:
        if a == '-1':
            cnt += 1
    for _ in range(cnt):
        line.remove('-1')

    LINE = ''.join(line)
if LINE == '':
    print('FRULA')
else:
    print(LINE)


