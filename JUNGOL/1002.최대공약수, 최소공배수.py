n = int(input())
arr = list(map(int, input().split()))

def gcd_get(a, b):
    for i in range(a, 0, -1):
        if a % i == 0:
            if b % i == 0:
                return i

gcd = lcm = arr[0]
for i in range(n):
    gcd = gcd_get(gcd, arr[i])
    lcm = lcm // gcd_get(lcm, arr[i]) * arr[i]

print(gcd, lcm)

