def seq_search(a, n, k):
    i = 0
    while i < n and a[i] != k:
        i += 1

arr = [4, 9, 11, 23, 2, 19, 7]
key = 23
print(seq_search(arr, len(arr), key))