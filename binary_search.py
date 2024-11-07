def binary_search(elements, low, high, target):
    while low <= high:
        mid = low + (high - low) // 2
        
        if elements[mid] == target:
            return mid
        
        elif elements[mid] < target:
            low = mid + 1
            
        else:
            high = mid - 1
    return -1

if __name__ == '__main__':
    elements = [1, 3, 5, 7, 9, 11, 13, 15]
    target = int(input("Enter target number: ")) 
    
    result = binary_search(elements, 0, len(elements)-1, target)
    if result != -1:
        print("Element is at index: ", result)
    else:
        print("Element does no exist")