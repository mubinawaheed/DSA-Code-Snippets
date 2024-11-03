from singlyLinkedList import LinkedList

class Stack:
    def  __init__(self):
        self.elements = LinkedList()

    def push(self, val):
        self.elements.insert(val)
        
    def pop(self):
        self.elements.delete()
        
    def isEmpty(self):
        return self.elements.head is None
    
stack = Stack()
stack.push(2)
stack.push(22)
stack.push(222)
stack.pop()
stack.pop()
stack.pop()
print("hi")