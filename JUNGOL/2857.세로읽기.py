import sys
sys.stdin = open('input.txt', 'r')

arr = [input() for _ in range(5)]
long = len(arr[0])
for i in arr:
    if len(i) > long:
        long = len(i)


for j in range(5):
    if len(arr[j]) != long:
        arr[j] = arr[j] + '?' *(long - len(arr[j]))

tmp = ''
for i in range(long):
    for j in range(5):
        tmp += arr[j][i]
print(tmp.replace('?', ''))
