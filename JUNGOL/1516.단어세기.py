import sys
sys.stdin = open('input.txt')

dic = {}

while 1:
    line = input().split()
    line.sort()
    if line[0] == 'END':
        break

    for i in line:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    print(dic)

