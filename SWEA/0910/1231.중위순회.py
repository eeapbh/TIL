def inOrder(v):
    if len(arr[v]) >=3:
        inOrder(int(arr[v][2]))
    print(arr[v][1], end='')
    if len(arr[v]) == 4:
        inOrder(int(arr[v][3]))


for tc in range(1, 11):
    v = int(input())
    arr = [[]]
    for i in range(1, v+1):
        arr.append(input().split())

    print('#{}'.format(tc), end=' ')
    inOrder(1)
    print()


