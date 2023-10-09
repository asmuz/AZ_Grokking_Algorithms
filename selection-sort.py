def FindSmallest(arr):
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex

def SelectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = FindSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (SelectionSort([5, 3, 6, 2, 10]))