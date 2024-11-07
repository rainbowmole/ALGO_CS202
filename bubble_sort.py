def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j +1 ] = arr[j + 1], arr[j]
    return arr

arr = [10, 13, 1, 4, 19, 3, 2, 5, 7, 25]
print("Original: ", arr)
print("sorted: ", bubble_sort(arr))