print(ord('A'))
info = 'SSADADAAASADAAAS'
m = len(info)
n = 5

check = [0]*27
for i in range(0, m-n+1):
    tmp = info[i:i+n]
    for t in tmp:
        check[ord(t)-65] += 1



print(chr(check.index(max(check))+65))