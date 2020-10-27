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
        bin = str(format(hx, 'b'))

        if len(bin) < 4:
            a = '0' * (4 - len(bin))
            bin = a + bin
            # bin.zfill(4)
        Bin += bin
    return Bin

def check(startIdx, Bcode):
    if startIdx < 55:
        return

    for i in range(startIdx, -1, -1):
        for j in range(8):
            c2 = c3 = c4 = 0
            while Bcode[i] == '1':
                c4 += 1
                i -= 1

            while Bcode[i] == '0':
                c3 += 1
                i -= 1

            while Bcode[i] == '1':
                c2 += 1
                i -= 1
            while Bcode[i] == '0':
                i -= 1

            m = min(c2, c3, c4)
            c2 = c2 // m
            c3 = c3 // m
            c4 = c4 // m
            c1 = 7-(c2+c3+c4)
            print(c1, c2, c3, c4)

            numList.append(P[(c1, c2, c3, c4)])
            startIdx = i

    check(startIdx, Bcode)


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    remember = []  # 16진수 가져오는거 기억할꺼
    for i in range(n):
        line = input()
        for j in line:
            if line == '0' * m or line in remember:
                continue
            if j != 0:
                number16 = line[:]
                remember.append(number16)
                Bcode = binCode(number16)

                for i in range(len(Bcode)-1, -1, -1):
                    if Bcode[i] == '1':
                        startIdx = i
                        break
                numList = []
                check(startIdx, Bcode)
    print(numList)




