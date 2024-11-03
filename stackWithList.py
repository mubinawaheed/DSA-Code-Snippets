class Stack:
    def __init__(self):
        self.elements = [] # takes 72 bytes in memory
        
    def push(self, val):
        self.elements.append(val)
    
    def isEmpty(self):
        return len(self.elements) == 0
    
    def pop(self):
        if not self.isEmpty():
            return self.elements.pop()
        raise Exception("Stack underFlow")


stack = Stack()
stack.push(3)
stack.push(13)
stack.push(23)
print(stack.pop())