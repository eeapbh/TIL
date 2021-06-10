import sys
sys.stdin = open('input.txt')

while 1:
    dic = {}
    line = input().split()
    line.sort()
    if line[0] == 'END':
        break

    for i in line:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    for k, v in dic.items():
        print('{} : {}'.format(k, v))




