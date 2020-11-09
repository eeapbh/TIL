import sys
sys.stdin = open('input.txt', 'r')
line = list(input())
n = len(line)
ans = ['']*n

# 65~90
check = [0]*26 # A~Z까지 몇개씩 있나 확인
for i in line:
    check[ord(i)-65] += 1 # 받은문자열 돌면서 그알파벳 있을때마다 1씩 추가

cnt = 0
idx = -1
oddidx = -1
for i in range(26):
    if check[i] % 2 != 0:
        cnt += 1
        for _ in range(1+check[i]//2):
            oddidx += 1
            ans[n//2 + oddidx] = ans[n//2-oddidx] = chr(65+i)
        if cnt > 1:
            rs = "I'm Sorry Hansoo"
            break

    elif check[i] % 2 == 0 and check[i] > 0:

        for _ in range(check[i]//2):
            idx += 1
            ans[idx] = ans[n-idx-1] = chr(65+i)
    rs = ''.join(ans)

print(rs)
