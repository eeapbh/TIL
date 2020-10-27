from itertools import

arr = [0]
cnt = 0
while 1:
    try:
        node = int(input())
        arr.append(node)
    except:
        break
print(arr)
ans = [0]
for i in range(1, len(arr)):

