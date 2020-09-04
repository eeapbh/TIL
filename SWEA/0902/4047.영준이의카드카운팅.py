import sys
sys.stdin = open('input.txt', 'r')

def check(dic):
    result = []
    for value in dic.values():
        count = 0
        for i in value:
            if i > 1:
                result = 'ERROR'
                return result
            elif i == 0:
                count += 1
        result.append(count-1)
    return result


t = int(input())
for tc in range(1, t+1):
    S = [0] * 14
    D = [0] * 14
    H = [0] * 14
    C = [0] * 14
    dic = {'S':[0] * 14, 'D':[0] * 14, 'H':[0] * 14, 'C':[0] * 14, }
    text = input()
    for t in range(len(text)):
        if t%3 == 0:
            k = text[t]
            number = ''
        elif t%3 == 1:
            number += text[t]
        elif t%3 == 2:
            number += text[t]
            v = int(number)
            dic[k][v] += 1
    checked = check(dic)
    print('#{}'.format(tc), end= ' ')
    if type(checked) == str:
        print(checked)
    else:
        for i in checked:
            print(i, end=' ')
        print()


