arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

arr2 = list(zip(*arr))
arr3 = list(zip(*arr2))
print(arr2)
print(arr3)
