t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(n):
        stack1 = []
        stack2 = []
        count1 = 0
        count2 = 0
        for j in range(n):
            stack1.append(arr[i][j])
            stack2.append(arr[j][i])
            if arr[i][j] == 1:
                count1 += 1
            if arr[j][i] == 1:
                count2 += 1

            if stack1[-1] == 0:

                if count1 == k:
                    count1 = 0
                    result += 1
                count1 = 0
            if stack2[-1] == 0:

                if count2 == k:
                    count2 = 0
                    result += 1
                count2 = 0
        if count1 == k:
            result += 1
        if count2 == k:
            result += 1



    print('#{} {}'.format(tc, result))



