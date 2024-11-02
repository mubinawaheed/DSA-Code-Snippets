class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
# implement search, insert, traverse, delete and len functions for it
class LinkedList:
    def __init__(self):
        self.head = None # head points to the first node
        self.size = 0
        
    def insert(self, value): #inserts a node at the beginning
        node = Node(value)
        node.next = self.head
        self.head = node
        
    def __len__(self):
        count=0
        currentPointer =  self.head
        while currentPointer is not None:
            count+=1
            currentPointer = currentPointer.next
        return count
    
    def traverse(self):
        print("Traversing linked list!...")
        if(self.head is None):
            print("Empty list")
            return False
        pointer=self.head
        while pointer is not None:
            print(f'Node value: {pointer.data}')
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

def insertAfter(head, x, value): # insert a node after the node containing x
    nodeX = head.search(x)
    if(nodeX[0]==True):
        node = Node(value)
        node.next = nodeX[2].next
        nodeX[2].next = node
    return head
            
def  insertBefore(head, x, value): # delete a node after the node containing x
    nodeX = head.search(x)
    node = Node(value)
    node.next = nodeX[2]
    
    if(nodeX[0]==True):
        if (nodeX[1] is None):
            head.head =  node
        else:
           nodeX[1].next = node
    return  head

def insertTailNode(head, value):
    if head.head is None:
        head.insert(value)
    else:
        a=head.head
        while a.next is not None:
            a=a.next
        node = Node(value)
        a.next = node
    return head
        

            
    
def deleteNodeContainingX(head,  x): # delete a node containing x
    nodeX = head.search(x)
    if(nodeX[0]==True):
        if(nodeX[1] is None):
            head.delete()
        else:
            nodeX[1].next = nodeX[2].next
    return head

def buildList(lst):
    assert  len(lst) > 0,  "List is empty"
    head = LinkedList()
    head.insert(lst[-1])
    a=head
    for  i in range(len(lst)-2, -1, -1):
        a.insert(lst[i])
    return  head

def circularizeSLL(pointer): # converts a SLL into circular SLL
    if pointer is None:
        return "Empty lst"
    a=pointer
    while a.next is not None:
        a=a.next
    a.next=pointer
    return pointer

def linearizeCSLL(pointer): # converts  a CSLL into SLL O(n)
    if pointer is None:
        return "Empty lst"
    a=pointer
    while a.next is not pointer:
        a=a.next
    a.next = None
    return pointer

def traverseCircularSSL(pointer):  # traverse a circular SLL O(n)
    if pointer is None:
        return "Empty lst"
    a=pointer
    while a.next is not pointer:
        print(a.data, end=" ")
        a=a.next
    print(a.data)


        
lst=buildList([1,2,3,4])
print("TYPE:",type(lst))
lst.traverse()
circularizeSLL(lst.head)
# lst.traverse() # POV it is a CSLL: It will get stuck in the traverse function because it wont find any node with next set to none:
# linearizeCSLL(lst.head)
traverseCircularSSL(lst.head)