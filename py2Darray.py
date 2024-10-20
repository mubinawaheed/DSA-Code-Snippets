from pyarray  import Array

class Array2D:
    
    def __init__(self, rows, cols, initialValue): #time complexity = O(r)
        self.numRows = rows
        self.numCols = cols
        self.theRows = Array(rows)
        
        for i in range(rows-1):
            self.theRows[i]=Array(cols,  initialValue)

            
    def clear(self, value): #time complexity = O(rc)
        for i in range(self.numRows-1):
            self.theRows[i].clear(value)
            
    def __getitem__(self, pos):
        assert  isinstance(pos, tuple), "pos must be a tuple"
        assert len(pos) == 2, "pos must be a tuple of two elements"
        assert  (0 <= pos[0] < self.numRows) and (0<=pos[1]<self.numCols), "row column index out of range"

        return self.theRows[pos[0]][pos[1]]
    
    def __setitem__(self, pos, value):
        assert  isinstance(pos, tuple), "pos must be a tuple"
        assert len(pos) == 2, "pos must be a tuple of two elements"
        assert  (0 <= pos[0] < self.numRows) and (0<=pos[1]<self.numCols), "row column index out of range"

        self.theRows[pos[0]][pos[1]] = value
        
    def traverse(self):  #time complexity = O(rc)
        for i in range(self.numRows-1):
            for j in range(self.numCols-1):
                print(self.theRows[i][j], end=" ")
            print()
            
array2d = Array2D(5,5,5)
array2d.traverse()