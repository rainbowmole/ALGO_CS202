def search(elements, target):
    for i in range(0, len(elements)):
        if (elements[i] == target):
            return i
    return -1

if __name__ == "__main__":
    elements = []
    while True:
        set_el = int(input("Input element in the array: "))
        set_el.append(elements)
        con = input("Continue[1] No[2]: ") 
        if con == 1: 
            continue
        else:
             False
             break
    target = int(input("Enter target number: "))    
        
    result = search(elements, target)
    if(result == -1):
        print("Element does not exist")
    else:
        print("Element at index: ", result)