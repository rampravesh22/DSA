def binarySearch(arr, start, end, target):
    if start > end:
        return -1
    mid = (end - start) // 2 + start
    if arr[mid] == target:
        return mid
    if target > arr[mid]:
        return binarySearch(arr, start + 1, end, target)
    else:
        return binarySearch(arr, start, end - 1, target)

ans = binarySearch([23,45,67,89,123],0,4,89)
print(f"index of target serach :",ans)