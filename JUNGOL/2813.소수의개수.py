# import math
# def prime(x):
#     if x == 1:
#         return 0
#     elif x == 2:
#         return 1
#     elif x > 2:
#         c = 0
#         for i in range(2, int(math.sqrt(x))+1):
#             if x % i == 0:
#                 c += 1
#         if c == 0:
#             return 1
#         else:
#             return 0

n, m = map(int, input().split())
arr = [0]*(m+1)

def eratos(x):
    arr[0] = -1
    arr[1] = -1
    for i in range(2, m+1):
        if arr[i] == 0:
            for j in range(i*i, m+1, i):
                arr[j] = -1
eratos(m)
cnt = 0
for i in range(n, m+1):
    if arr[i] == 0:
        cnt += 1
print(cnt)


