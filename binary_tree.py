from collections import deque
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return

        q = deque()
        q.append(self.root)
        
        while q:
            curr = q.popleft()
            if curr.left is None:
                curr.left = node
                return
            q.append(curr.left)
            
            if curr.right is None:
                curr.right = node
                return
            
            q.append(curr.right)
    
    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.value, end=" ")
        self.in_order(node.right)
        
    def pre_order(self, node):
        if node is None:
            return
        print(node.value, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)
    
    def post_order(self, node):
        if node == None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.value, end=' ')

if __name__ == "__main__":
    arr: list = [10, 6, 15, 3, 8, 12, 20]
    tree = BinaryTree()
    
    for value in arr:
        tree.insert(value)
        
    print("In-order Traversal:")
    tree.in_order(tree.root)
    print("\nPre-order Traversal:")
    tree.pre_order(tree.root)
    print("\nPost-order Traversal:")
    tree.post_order(tree.root)
   

    
    
