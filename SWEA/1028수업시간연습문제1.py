def SelectionSort(arr, idx):
    min = idx
    if idx == len(arr)-1:
        return
    for i in range(idx+1, len(arr)):
        if arr[idx] > arr[i]:
            min = i
        arr[idx], arr[min] = arr[min], arr[idx]
    SelectionSort(arr, idx+1)



arr = [3, 2, 5, 1, 6, 4]
SelectionSort(arr, 0)
print(arr)
