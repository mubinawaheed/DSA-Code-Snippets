#this file includes code for Array implementation in python
#in an array of 10 elements we can only add 9 elements. The last element is always empty


import ctypes

class Array():
    def __init__(self, n):
        assert n > 0 , 'Array cannot contain 0 elements'
        self.size = n
        self.elements = (ctypes.py_object * n)()
        self.clear(None) # will place none in all elements of array
        
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        assert index >= 0 and index < self.size , "Invalid index"
        return self.elements[index]
    
    def __setitem__(self, index, value):
        assert index >= 0 and index < self.size , "Invalid index"
        self.elements[index]= value
        
    def insert(self, index, value): #inserts an element at index 
        for i in range(self.size-1, index+1):
           self.elements[i] = self.elements[i-1]
        
        self.elements[index] = value
        
    def delete(self, index):
        for i in range(index, self.size-1):
            self.elements[i] = self.elements[i+1]
        self.elements[self.size-1]=None
            
    def traverse(self):
        for i in range(self.size -1 ):
            print(self.elements[i])
        
    def clear(self, value):
        for i in range(self.size -1):
            self.elements[i]=value
            
