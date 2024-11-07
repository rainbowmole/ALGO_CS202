class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None    

class stack:
    def __init__(self):
        self.head = None
        self.next = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        
        if not new_node:
            print("/nStack Overflow")
            return
        
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.is_empty():
            print("\n Stack Underflow")
        else:
            temp = self.head
            self.head = self.head.next
            del temp

    def peek(self):
        if not self.is_empty():
            return f'top of the nodes: {self.head.data}'
        else:
            print('\nStack is empty')
            return float('inf')
    
    def is_empty(self):
        return self.head is None
    
    def view(self):
        if self.is_empty():
            print("\n Stack Underflow")
        else:
            temp = self.head
            while(temp != None):
                print(f'{temp.data} <- ', end = '')
                temp = temp.next
            print()
            
    def count_nodes(head):
        count = 0
        curr = head
        
        while curr is not None:
            count += 1
            curr = curr.next
            
        return f'current number for nodes in the stack: {count}'

stack = stack()

stack.push(7)
stack.push(14)
stack.push(21)
stack.push(28)
stack.view()
print(stack.peek())
stack.pop()
stack.pop()
stack.pop()
stack.view()
print(stack.count_nodes())
