from pyarray import Array
lst = Array(8)

for i in range(lst.size-1):
    lst[i] = i+1
    
lst.traverse()
def binarySearch(array, element):
    start=0
    end = len(array) - 1
    while start<=end:
        mid = (start+end) // 2
        if(array[mid] == element):
            return mid
        elif (array[mid]<element):
           start = mid+1
        elif(array[mid]>element):
            end = mid-1
    return None

n=binarySearch(lst.elements, 4)
print("FOUND", n)