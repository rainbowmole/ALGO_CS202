class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.value = key
        
def insert(root, key):
    if root is None:
        return Node(key)
    if root.value == key:
        return root
    if root.value < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root
    
def search(root, value):
    if root.value == value:
        return True
        
    if value < root.value:
        if root.left is None:
            return False
        return search(root.left, value)
        
    if root.right is None:
        return False
    return search(root.right, value)
        
def height( root):
    if root is None:
        return -1
        
    lheight = height(root.left)
    rheight = height(root.right)
        
    return max(lheight, rheight) + 1
    
if __name__ == "__main__":
    arr: list = [10, 6, 15, 3, 8, 12, 20]
    root = Node(arr.pop(0))
    for x in arr:
        root = insert(root, x)
            
    print(f"searching for 6: {search(root, 6)}")
    print(f"Searchin for 21: {search(root, 21)}")
    print(f"height of the tree: {height(root)}")
    
        