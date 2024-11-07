def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 #divides the array in two
        left_half = arr[:mid] #put left half elements in another array
        right_half = arr[mid:] #put right half elements in another array
        
        merge_sort(left_half) #sorting the left half
        merge_sort(right_half) #sorting the right half

        i = j = k = 0
        
        #merges two sorted elements back into the array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]: 
                arr[k] = left_half[i]
                i += 1
                print(arr)
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        #the remaining elements in the left is appended
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        #the remaining elements in the left is appended
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        
    return arr #returns the sorted list

arr = [38, 27, 43, 3, 9, 82, 10]
print("Original: ", arr)
print("sorted: ", merge_sort(arr))