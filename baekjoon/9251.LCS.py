import sys
sys.stdin = open('input.txt', 'r')

a = input()
b = input()
cnt = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            cnt += 1
            break


print(cnt)