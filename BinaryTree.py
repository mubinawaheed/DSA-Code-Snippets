from typing import List, Optional


class BinaryTree:
    def __init__(self, val):
        self.rc=None
        self.lc=None
        self.data = val
        
    def insertRight(self, val):
        if self.rc is None:
            self.rc = BinaryTree(val)
            
    def insertLeft(self, val):
        if self.lc is None:
            self.lc = BinaryTree(val)
            
    def deleteLeftChild(self): # It deletes a left child of a node pointed to by self. And the left child must be a leaf node.
        assert self.lc is not None, "Left child absent"
        assert self.lc.lc is not None or self.lc.rc is not None, "Can only delete a leaf node"
        x = self.lc.data
        self.lc = None
        return x
    
    def deleteRightChild(self): # It deletes a left child of a node pointed to by self. And the left child must be a leaf node.
        assert self.rc is not None, "right child absent"
        assert self.rc.lc is not None or self.rc.rc is not None, "Can only delete a leaf node"
        x = self.rc.data
        self.rc = None
        return x
    
    def height(self):
        if(self.rc is None and self.lc is None):
            return 1
        rh=0
        lh=0
        if(self.rc is not None):
            rh=self.rc.height()
        if(self.lc is not None):
            lh=self.lc.height()
        if (rh>lh):
            return 1+rh
        return 1+lh
    
    def nodeCount(self):
        if(self.rc is None and self.lc is None):
            return 1
        lnc =0
        rnc =0
        
        if(self.rc is not None):
            rnc = self.rc.nodeCount()
            
        if(self.lc is not None):
            lnc = self.lc.nodeCount()
        return 1+lnc+rnc
    
    def leafCount(self):
        if(self.rc is None and self.lc is None):
            return 1
        lnc =0
        rnc =0
        
        if(self.rc is not None):
            rnc = self.rc.leafCount()
            
        if(self.lc is not None):
            lnc = self.lc.leafCount()
        return lnc+rnc
    
    def isStrictlyBT(self):
        if self.lc is None:
            if self.rc is None:
                return True
            return False
        
        if self.rc is None:
            return False
        
        return self.lc.isStrictlyBT() and self.rc.isStrictlyBT()
    
    def isPerfectBT(self):
        h = self.height()
        n = self.nodeCount()
        m = pow(2,h) -1
        return n == m   
    
    def insert(self, data): # it builds a binary search tree
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.lc is None:
                    self.lc = BinaryTree(data)
                else:
                    self.lc.insert(data)
            elif(data>self.data):
                if self.rc is None:
                    self.rc = BinaryTree(data)
                else:
                    self.rc.insert(data)
  
    def build(self, lst): # requires a list in pre-orderal - Not Correct
        leftSubTree = lst[1:(len(lst)//2)+1]
        self.lc = BinaryTree(leftSubTree[0])
        if(len(leftSubTree)>1):
            self.lc.build(leftSubTree)
            
        
        rightSubTree = lst[len(lst)//2 + 1:]
        self.rc = BinaryTree(rightSubTree[0])
        if(len(rightSubTree)>1):
            self.rc.build(rightSubTree)
        return self
    
    def inOrderTraversal(self):
        res=[]
        def inOrder(root):
            if(root.lc is not None):
                # root.lc.inOrderTraversal()
                inOrder(root.lc)
            # print(self.data, end=' ')
            res.append(root.data)
            if(root.rc is not None):
                # root.rc.inOrderTraversal()
                inOrder(root.rc)
        inOrder(self)
        return res

lst = [1,2,4,5,3,6,7]
bt = BinaryTree(lst[0])
tree=bt.build(lst)
print(tree.inOrderTraversal())