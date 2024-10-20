import time

#time complexity worst case = O(n^2)
#time complexity best case = O(n^2)
def bubbleSort(array):
    start = time.time()
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if(array[j]>array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    end = time.time()
    print("Total time = ", end-start)
    return array

array = list(range(1, 10001)) #took 4.1 seconds
wb= bubbleSort(array)
print("Sorted array -nonotp", wb)


#Best case time complexity = O(n)
#worst case time complexity = O(n^2)
def bubbleSortOptimized(array):
    start = time.time()
    for i in range(len(array)-1):
        swap = False
        for j in range(len(array)-1-i):
            if(array[j]>array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
                swap = True
        if(not swap):
            print("Array is already sorted", i)
            break
    end = time.time()
    print("Total time = ", end-start)
    return array

ascending_array = list(range(1,10001))
b=bubbleSortOptimized(ascending_array) # took 2 miliseconds for pre-sorted array
print("sorted array", b)

