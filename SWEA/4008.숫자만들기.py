import sys
from itertools import permutations
sys.stdin = open('input.txt', 'r')

t = int(input())
# dic = {'+':0, '-':0, '*':0, '/':0}
dic = ['+', '-', '*', '/']
for tc in range(1, t+1):
    n = int(input())
    cal = list(map(int, input().split()))
    number = list(map(int, input().split()))
    operator = []
    for i in range(4):
        for j in range(cal[i]):
            operator.append(dic[i])
    pnumber = list(permutations(number, n))
    poperator = list(permutations(operator, len(cal)))
    for pn in pnumber:
        f = pn[0]
        for po in poperator:
            for i in len(cal):
                eval(f+po[i])
    print(operator)
    # idx = 0
    # for d in dic:
    #     dic[d] = cal[idx]
    #     idx += 1
    # print(dic)

