def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr =  [43, 9, 2, 5, 27, 10, 14, 37, 13, 28, 1, 31]
print("Original: ", arr)
print("Sorted: ", selection_sort(arr))