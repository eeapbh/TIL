# number = input()
# a = int(number, 2)
# print(a)
num = list(input())
n = len(num)
ans = 0
for i in range(n-1, -1, -1):
    ans += 2 ** (n - i - 1) * int(num[i])
print(ans)
