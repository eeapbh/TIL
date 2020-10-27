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
    if startIdx <55:
        return -1
    for b in range(startIdx, -1, -1):
        pw = []
        numList = []
        cnt = 1
        if Bcode[b] == '1':  # 1인거 찾으면
            for idx in range(b, -1, -1):  # 앞으로 탐색하면서 숫자바뀔떄마다 카운트
                if Bcode[idx] == Bcode[idx - 1]:
                    cnt += 1
                else:
                    pw.append(cnt)
                    cnt = 1
                if len(pw) == 4:  # 카운트한거 길이가 4가 되면 비율이 나온거니까 비율체크하고 비번찾음
                    pw = reversed(pw)

                gcd = min(pw)
                for p in pw:
                    p = p // gcd  # 최종 비율을 구함
                num = P[pw]  # 비율구한걸로 숫자구함
                numList.append(num)
                if len(numList) == 8:
                    save.append(numList)
                    numList = []
                leng = gcd * 56
                startIdx = idx - leng
                return check(startIdx, Bcode)

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    save = []
    for i in range(n):
        line = input()
        if line == '0'*m:
            continue
        for j in range(m):
            if line[j] != '0': # 0아닌거있으면 일단 그줄 다가져옴
                number = line[:]
        Bcode = binCode(number) # 이진으로 바꿈

        for b in range(len(Bcode)-1, -1, -1):
            pw = []
            numList = [] #8개짜리 숫자
            cnt = 1
            if Bcode[b] == '1': # 1인거 찾으면
                for idx in range(b, -1, -1): # 앞으로 탐색하면서 숫자바뀔떄마다 카운트
                    if Bcode[idx] == Bcode[idx-1]:
                        cnt += 1
                    else:
                        pw.append(cnt)
                        cnt = 1
                    if len(pw) == 4: # 카운트한거 길이가 4가 되면 비율이 나온거니까 비율체크하고 비번찾음
                        pw = list(reversed(pw))
                        break

                gcd = min(pw)
                for p in pw:
                    p = p//gcd # 최종 비율을 구함
                num = P[tuple(pw)] #  비율구한걸로 숫자구함
                numList.append(num)
                if len(numList) == 8:
                    save.append(numList)
                    numList = []
                leng = gcd * 7
                startIdx = idx - leng
                if check(startIdx, Bcode) == -1:
                    break
    print(save)






