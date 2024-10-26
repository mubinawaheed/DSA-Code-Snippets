class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
# implement search, insert, traverse, delete and len functions for it
class LinkedList:
    def __init__(self):
        self.head = None # head points to a node
        self.size = 0
        
    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        
    def __len__(self):
        count=0
        currentPointer =  self
        while currentPointer is not None:
            count+=1
            currentPointer = currentPointer.next
        return count
    
    def traverse(self):
        if(self.head is None):
            print("Empty list")
            return False
        pointer=self.head
        while pointer is not None:
            print(f'Node value: {pointer.data}', end=" ")
            pointer = pointer.next
        
    def search(self, target): # returns the pointer of the node before target node and the target node
        a  = self.head
        
        if(a.data == target):
            return [True, None, a]
        b=a.next
        while  b is not None and  b.data != target:
            a=a.next
            b=b.next
        if(b is None):
            print("Node not found")
        return [b is not None, a , b]
    
    def  delete(self): # deletes a node after the node pointed to by self. i.e. first node
        if(self.head  is None):
            print("Empty linked list!...")
            return False
        temp = self.head.next
        self.head = self.head.next
        return temp

        
lst = LinkedList()
lst.insert(5)
lst.insert(4)
lst.insert(3)
lst.insert(2)
lst.insert(1)
node = lst.search(1)
print(node)

