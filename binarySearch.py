def binarySearch(list1, value):
    list2 = list1.copy()
    list2.sort()
    low = 0
    high = len(list2) - 1
    # mid = 0
    while low <= high:
        mid = low + (high - low) // 2
        if value > list2[mid]:
            low = mid + 1
        elif value < list2[mid]:
            high = mid - 1
        elif value == list2[mid]:
            a = list2[mid]
            return a
        else:
            return -1


list1 = list(map(int, input().split()))
print(list1)
value = int(input('Enter value to search:'))
a = binarySearch(list1, value)
print(f'Value at index {list1.index(a)} :', a)
