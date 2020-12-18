a = int(input())
b = int(input())
c = int(input())
num = a*b*c
num = str(num)
n = len(num)
ans = [0]*10
for i in range(n):
    ans[int(num[i])] += 1

for i in range(10):
    print(ans[i])