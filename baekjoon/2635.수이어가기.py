import sys
sys.stdin = open('input.txt', 'r')
#
# num = int(input())
#
# def check(tmp):
#     i = 0
#     while 1:
#         if tmp[i]-tmp[i+1] >=0:
#             tmp.append(tmp[i]-tmp[i+1])
#         else:
#             return tmp
#         i += 1
#
#
# result = []
# length = []
# for i in range(num//2, num):
#     if num == 1:
#         result = [[1, 1]]
#         length = [2]
#         break
#     tmp = [num]
#     tmp.append(i)
#     result.append(check(tmp))
#     length.append(len(tmp))
#
# print(max(length))
# idx = length.index((max(length)))
#
# print(*result[idx])
#
# N = int(input())

ans = []
maxlen = 0
for i in range(N,-1,-1):
    tmp = [N]
    K = i
    while K >= 0:
        tmp.append(K)
        K = tmp[len(tmp)-2]-tmp[len(tmp)-1]
    if len(tmp) > maxlen:
        maxlen = len(tmp)
        ans = tmp[:]

print(len(ans))
print(*ans)


