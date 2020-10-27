number = list(map(int, input()))

for i in range(0, len(number), 7):
    arr = number[i:i+7]
    total = 0
    for j in range(6, -1, -1):
        k = (6-j)
        total += arr[j] * (2**k)
    if i == len(number)-7:
        print(total)
    else:
        print(total, end=', ')
