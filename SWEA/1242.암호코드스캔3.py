import sys
sys.stdin = open('input.txt', 'r')

P = {(3, 2, 1, 1): 0,
     (2, 2, 2, 1): 1,
     (2, 1, 2, 2): 2,
     (1, 4, 1, 1): 3,
     (1, 1, 3, 2): 4,
     (1, 2, 3, 1): 5,
     (1, 1, 1, 4): 6,
     (1, 3, 1, 2): 7,
     (1, 2, 1, 3): 8,
     (3, 1, 1, 2): 9}

def binCode(code):
    Bin = ''
    for i in range(len(code)):
        hx = int(code[i], 16)
        bins = str(format(hx, 'b'))

        if len(bins) < 4:
            a = '0' * (4 - len(bins))
            bins = a + bins
            # bin.zfill(4)
        Bin += bins
    return Bin

def check(startIdx, Bcode):

    for i in range(startIdx, -1, -1):
        idx = i
        while 1:
            c2 = c3 = c4 = 0
            while Bcode[idx] == '1':
                c4 += 1
                idx -= 1

            while Bcode[idx] == '0':
                c3 += 1
                idx -= 1

            while Bcode[idx] == '1':
                c2 += 1
                idx -= 1
            m = min(c2, c3, c4)
            c4 = c4 // m
            c3 = c3 // m
            c2 = c2 // m
            c1 = 7 - (c2 + c3 + c4)

            # print(c1, c2, c3, c4)
            # print(P[(c1, c2, c3, c4)])

            numList.append(P[(c1, c2, c3, c4)])
            while Bcode[idx] == '0':
                if idx == 0:
                    return
                idx -= 1






t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    remember = []  # 16진수 가져오는거 기억할꺼 봤던코드면 바로넘기기위해
    numList = []   # 코드8개짜리구한거 저장해놓는용도
    for i in range(n):
        line = input()
        for j in line:
            if line == '0' * m or line in remember: # 0만있는줄이거나 봤던코드면 넘김
                continue
            if j != 0:  # 0 아닌 다른거 나오는거있으면
                number16 = line[:]
                remember.append(number16)   # 저장하고
                Bcode = binCode(number16)   # 2진수로 바꿈

                for i in range(len(Bcode)-1, -1, -1):   # 뒤에서부터 돌다가 1찾으면 함수시작함
                    if Bcode[i] == '1':
                        startIdx = i
                        break

                check(startIdx, Bcode)
    # print(numList)
    ans = 0
    numList = list(reversed(numList))   # 함수다돌고나면 숫자들 쭉쌓여있음 길이는 8의배수일꺼임
    Check = []
    for i in range(0, len(numList), 8):
        pwCheck = numList[i:i+8]    # 8씩 쪼개면서

        if pwCheck in Check:    # 이미 계산한 코드면 넘김
            continue
        Check.append(pwCheck)
        odd = 0
        even = 0

        for idx in range(7):
            if idx % 2 == 0:
               odd += pwCheck[idx]
            else:
                even += pwCheck[idx]
        if (odd*3 + even + pwCheck[7]) % 10 == 0:
            ans += sum(pwCheck)
    print('#{} {}'.format(tc, ans))



