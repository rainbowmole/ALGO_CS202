class stack:
    def __init__(self):
        self.stacks = []
    
    def push(self, item):
        self.stacks.append(item)
        print("\npushing ", item, "in the stack")
    
    def pop(self):
        if not self.is_empty():
            print(f'Popping: {self.stacks[-1]}\n')
            return self.stacks.pop()
        print('Stack is Empty')

    def peek(self):
        if self.is_empty():
            return None
        
        return f'Currently at the top of the stack: {self.stacks[-1]}\n'
    
    def is_empty(self):
        return len(self.stacks) == 0 
    
    def size(self):
        return f'Number of items in the stack: {len(self.stacks)}\n'
            
    def __str__(self):
        if self.is_empty() == True:
            return 'stack is empty'
                
        return f'Stack: {str(self.stacks)}\n'

stack = stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)
print(stack)
print(stack.peek())
stack.pop()
stack.pop()
print(stack)
print(stack.size())