def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)
    return arr

arr = [12, 11, 13, 5, 6]
print("Original: ", arr)
print("Sorted: ", insertion_sort(arr))