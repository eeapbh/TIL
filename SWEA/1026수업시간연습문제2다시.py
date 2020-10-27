import sys
sys.stdin = open('input.txt', 'r')
# 01D06079861D79F99F
n = input()
Bin = ''
for i in range(len(n)):
    hx = int(n[i], 16)
    bin = str(format(hx, 'b'))

    if len(bin) < 4:
        a = '0'*(4-len(bin))
        bin = a+bin
        #bin.zfill(4)
    Bin += bin
print(Bin)
save = []
for i in range(0, len(Bin), 7):
    tmp = Bin[i:i+7]
    total = 0
    for j in range(len(tmp)):
        if tmp[len(tmp)-1-j] == '1':
            total += 2**j
    save.append(total)

for i in range(len(save)):
    if i == len(save)-1:
        print(save[i])
    else:
        print(save[i], end=', ')