class BTree:
    def __init__(self, val):
        self.rc=None
        self.lc=None
        self.data = val
        
    def insertRight(self, val):
        if self.rc is None:
            self.rc = BTree(val)
            
    def insertLeft(self, val):
        if self.lc is None:
            self.lc = BTree(val)
            
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