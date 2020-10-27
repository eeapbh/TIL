import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):

    a, n = input().split()
    Bin = ''
    for i in range(len(n)):
        hx = int(n[i], 16)
        bin = str(format(hx, 'b'))

        if len(bin) < 4:
            a = '0'*(4-len(bin))
            bin = a+bin
            #bin.zfill(4)
        Bin += bin
    print('#{} {}'.format(tc, Bin))

