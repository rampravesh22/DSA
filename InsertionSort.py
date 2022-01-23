def insertionSort(arr):
    for i in range(1, len(arr)):
        currentElement = arr[i]
        pos = i
        while currentElement < arr[pos - 1] and pos > 0:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = currentElement


print(insertionSort([5, 75, 595, 85881, 2, 3, 4]))
