import sys
sys.stdin = open('input.txt', 'r')

# 별, 동그라미, 네모, 세모
# 4,  3,         2,    1
n = int(input())
for i in range(n):
    tmp1 = list(map(int, input().split()))
    tmp2 = list(map(int, input().split()))
    tmp1[0] = 0
    tmp2[0] = 0
    if tmp1.count(4) > tmp2.count(4):
        print('A')
    elif tmp1.count(4) < tmp2.count(4):
        print('B')
    else:
        if tmp1.count(3) > tmp2.count(3):
            print('A')
        elif tmp1.count(3) < tmp2.count(3):
            print('B')
        else:
            if tmp1.count(2) > tmp2.count(2):
                print('A')
            elif tmp1.count(2) < tmp2.count(2):
                print('B')
            else:
                if tmp1.count(1) > tmp2.count(1):
                    print('A')
                elif tmp1.count(1) < tmp2.count(1):
                    print('B')
                else:
                    print('D')
