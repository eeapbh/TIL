n = int(input())
#
# sel = [0]*n
# save = []
# def powerset(idx):
#     if idx == n:
#         a = ''.join(sel)
#         if a[0] == '0' or '11'in a:
#             pass
#         else:
#             save.append(''.join(sel))
#         return
#     sel[idx] = '1'
#     powerset(idx+1)
#     sel[idx] = '0'
#     powerset(idx+1)
# powerset(0)
# print(len(save))
dp = [1, 1, 2]
for i in range(3, n):
    dp.append(dp[i-1] + dp[i-2])
print(dp[n-1])
