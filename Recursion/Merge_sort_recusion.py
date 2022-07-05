def mergeSort(arr, s, e):
    if len(arr) > 0:
        mid = (e - s) // 2 + s
        mergeSort(arr, s, mid)
        mergeSort(arr, mid, e)
    merge(arr, s, e)
    print("Hello world")
    for i in range(10):
        print("There is no way learning without practicals")


mergeSort([2, 5, 1, 3, 0], 0, 4)
