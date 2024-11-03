class DLLNode:
    def __init__(self, value):
        self.right=None
        self.left=None
        self.data = value
        
    def insertRight(self, val):
        node = DLLNode(val)
        q = self.right
        node.right = self.right
        node.left = self
        self.right = node
        if(q is not None):
            q.left = node
            
    def insertLeft(self, val):
        r = self.left
        node = DLLNode(val)
        node.right = self
        node.left =self.left
        self.left = node
        if(r is not None):
            r.right = node
        
    def traverse(self):
        a = self
        while a.left is not None:
            a = a.left
        while a is not None:
            print(a.data, end=" ")
            a = a.right
        print()
        
    def __len__(self):
        a = self
        count = 0
        while a is not None:
            count += 1
            a = a.right
        b= self.left
        while b is not None:
            count += 1
            b = b.left
        return count
    
    def delete(self):
        if(self is None):
            return None
        q = self.right
        r = self.left
        if(r is None):
            q.left = self.left
            return q
        if(q is None):
            r.right = self.right
            return  r
        r.right = q
        q.left = r
        return r
    
    def  search(self, val):
        b = self
        while b is not None and b.data !=val:
            b = b.right
        if b is not None:
            return b
        b = self.left
        while b is not None and b.data != val:
            b = b.left
        if b is not None:
            return b
        
        return "Not found"

        
        
dll = DLLNode(4)
# dll.insertLeft(5)
# dll = dll.delete()
# dll.traverse()
dll.insertRight(6)
dll.insertRight(7)
dll.insertLeft(3)
dll.insertRight(17)
dll.traverse()
dll=dll.delete()
dll.traverse()
dll.insertLeft(2)
dll.traverse()
dll.insertRight(16)
dll = dll.delete()
dll.traverse()
node=dll.search(171)
print("FOUND", node.data)
print("Length of list",len(dll))