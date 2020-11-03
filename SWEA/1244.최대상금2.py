import sys
sys.stdin = open('input.txt', 'r')


def check(arr):
    global cnt
    if cnt == n:
        return
    new = []
    for i in range(1, length):
        new.append((arr[i], i))
    print(new)
    new.sort()
    print(new)
    for i in range(length):
        for j in range(length-2, 0, -1):
            if new[j][0] > arr[i]:
                idx = new[j][1]
                arr[idx], arr[i] = arr[i], arr[idx]
                cnt += 1
                return check(arr)


t = int(input())
for tc in range(1, t+1):
    number, n = input().split()
    length = len(number)
    arr = []
    for i in number:
        arr.append(i)
    print(arr)
    n = int(n)
    cnt = 0
    check(arr)
    print(arr)