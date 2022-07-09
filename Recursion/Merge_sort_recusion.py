""""
Algorithms
1- Split the unsorted list
2- Compare each of the elemnt and group
3 - Repeat step-2 until the whole list is merged and sorted
"""


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_list = arr[:mid]
        right_list = arr[mid:]
        mergeSort(left_list)
        mergeSort(right_list)
        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                arr[k] = left_list[i]
                i += 1
                k += 1
            else:
                arr[k] = right_list[j]
                j += 1
                k += 1
        while i < len(left_list):
            arr[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            arr[k] = right_list[j]
            j += 1
            k += 1
    return arr
string = "9 5 3 1 2 4"
arr = list(map(int, string.split()))
print(mergeSort(arr))
