arr = [[1, 2, 3], [4, 5, 6]]
arr2 = list(zip(*arr))
print(arr2)
print(sum(arr2[1]))