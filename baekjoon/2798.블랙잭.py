

t, target = map(int, input().split())
numbers = list(map(int, input().split()))

sum_num = 0
arr1 = []
arr2 = []
for i in range(t):
    for j in range(t):
        for k in range(t):
            if i != j and i != k and j != k:
                sum_num = numbers[i]+ numbers[j]+ numbers[k]
                arr1.append(sum_num)
                sum_num = 0
# 3개의 합경우를 모두 arr1에 모은다
# for문돌리면서 target을 뺀값을 arr2에 모은다.
# arr2의 value중에 0보다 큰거는 엄청작은값으로 바꿔준다
# max(arr2)의 index를 index1에 넣고
# arr1[index1] 출력

for i in arr1:
    arr2.append(i-target)

for i in range(len(arr2)):
    if arr2[i] > 0:
        arr2[i] = -1000000
index1 = arr2.index(max(arr2))
print(arr1[index1])
