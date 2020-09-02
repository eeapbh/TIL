import sys
N = int(sys.stdin.readline())
numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline()))
rs1 = round(sum(numbers)/N)
tmp = sorted(numbers)

rs2 = tmp[N//2]
counting = {}
for i in numbers:
    if i not in counting.keys():
        counting[i] = 1
    else:
        counting[i] += 1
max_count = max(counting.values())
save = []
for k, v in counting.items():
    if v == max_count:
        save.append(k)
save.sort()
rs3 = 0
if len(save) > 1:
    rs3 = save[1]
else:
    rs3 = save[0]

rs4 = max(numbers)-min(numbers)
print(rs1)
print(rs2)
print(rs3)
print(rs4)