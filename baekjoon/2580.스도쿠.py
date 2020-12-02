import sys
sys.stdin = open('input.txt', 'r')

arr = [list(map(int, input().split())) for _ in range(9)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def garo():
    for i in range(9):
        if arr[i].count(0) == 1:
            for j in range(9):
                if arr[i][j] == 0:
                    arr[i][j] = 45-sum(arr[i])

def sero():
    for i in range(9):
        if arr2[i].count(0) == 1:
            for j in range(9):
                if arr[j][j] == 0:
                    arr[j][i] = 45-sum(arr2[i])
garo()
arr2 = list(zip(*arr))
sero()
for a in arr:
    print(a)