def quickSort(array, left, right ):
    if left < right:
        pivot = partition(array, left, right)
        quickSort(array, left, pivot-1)
        quickSort(array, pivot+1, right)
        
def partition(array, left, right):
    i = left
    j = right-1
    pivot = array[right]
    while i<j:
        while  i<right and array[i]<pivot :
            i += 1
        while array[j]>=pivot and j>left:
            j-=1
        if i < j:
            array[i], array[j] = array[j], array[i]
        
    if(array[i]>pivot):
        array[i], array[right] = array[right], array[i]
        
    return i
array = [55,66,77,22,33,99,10]
quickSort(array,0, len(array)-1)

print(array)