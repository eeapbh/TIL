from math import gcd

import sys
sys.stdin = open('input.txt', 'r')

def binCode(code):
    Bin = ''
    for i in range(len(code)):
        hx = int(code[i], 16)
        bin = str(format(hx, 'b'))

        if len(bin) < 4:
            a = '0' * (4 - len(bin))
            bin = a + bin
            # bin.zfill(4)
        Bin += bin
    return Bin

def check(pwCode):
    count = 1
    bi = []
    for i in range(len(pwCode)-1, -1, -1):
        if pwCode[i] == '1':
            while len(bi) < 4:

                if pwCode[i] == pwCode[i-1]:
                    count += 1
                else:
                    bi.append(count)
                    count = 1
                i -= 1
        if len(bi) == 4:
            break
    bi = list(reversed(bi))
    num1 = num2 = 0
    for b in bi:
        if num1 == 0:
            num1 = b
        if b != num1:
            num2 = b
        if num1 != 0 and num2 != 0:
            break
    GCD = gcd(num1, num2)
    leng = GCD * 56

    mok = leng//56 #56으로 나눠서 몫곱하기 56만큼 앞으로 가기위해
    for i in range(len(pwCode)-1, -1, -1):
        if pwCode[i] == '1':
            realCode = pwCode[i+1-mok*56:i+1]
            return realCode, mok

arr = [
        [3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2],
        [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]
    ]
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    codes = []
    for i in range(n):
        line = input()
        code = ''
        for j in range(m):
            if line[j] != '0':
                code += line[j]
            if len(code) > 0:
                if line[j] == '000':
                    break
        if code not in codes and code != '':
            codes.append(code)
    # print(codes)
    sumDab = 0 # 암호 2개 이상일때 더할꺼
    bins = [] # 2진으로 바꾼코드 담을거
    for c in range(len(codes)):
        pwCode = '0'*m +binCode(codes[c])
        bins.append(binCode(codes[c]))
        # print('이진으로 바꾼거 길이', len(pwCode))
        realCode, mok = check(pwCode) # 그 이진에서 진짜 이진코드랑 몫뽑음
        # 진짜이진코드를 7곱하기아까나온 몫 만큼 슬라이싱하면서
        dab = []
        for i in range(0, len(realCode), mok*7 ):
            a = realCode[i:i+mok*7] # 진짜이진코드 7의배수씩 쪼갬
            # print(a)
            cnt = 1
            save = []

            for i in range(len(a)-1):
                if a[i] == a[i+1]:
                    cnt += 1
                else:
                    save.append(cnt//mok)
                    cnt = 1
                if i == len(a)-2:
                    save.append(cnt//mok)
                #해서 비율구하고
            # print('비율', save)
            dab.append(arr.index(save)) # 비율구한거 인덱스로 숫자뭔지찾음
        # print('dab', dab)
        total = 0
        odd = 0
        even = 0
        for idx in range(7):
            if idx % 2 == 0:
                odd += dab[idx]
            else:
                even += dab[idx]
        total = odd*3 + even + dab[7]

        if total % 10 == 0:
            sumDab += sum(dab)

    print('#{} {}'.format(tc, sumDab))
        # else:
        #     if c < len(codes)-1:
        #         continue
        #     else:
        #         print('#{} {}'.format(tc, 0))
        # 그 비율에 맞는 코드를 찾아서 암호검증을함

