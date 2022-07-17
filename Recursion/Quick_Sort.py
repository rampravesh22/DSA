"""
Quick sort algorithm:
    1. Select the pivot element.
    2. Find the correct position of the pivot element in the list by.
    3. Divide the list based on the pivot element.
    4. Sort the sublist recursively.

(a). For ascending order : <smaller value>  <pivot>  <bigger value>
(b). For descending order : <bigger value>  <pivot>  <smaller value>

Pivot element can be :
    1. First element.
    2. Last element.
    3. Any random element.
    4. Median of three value (first, middle, last)
"""


# Program

# To find the pivot element (If the pivot is the first element)
def pivot_place(arr, first_index, last_index):
    pivot = arr[first_index]
    left = first_index + 1
    right = last_index
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1

        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[first_index], arr[right] = arr[right], arr[first_index]    # arr[first_index] = pivot
    return right


def quickSort(arr, first_index, last_index):
    if first_index > last_index:
        return arr
    if first_index < last_index:
        p = pivot_place(arr, first_index, last_index)
        quickSort(arr, first_index, p - 1)
        quickSort(arr, p + 1, last_index)

arr = [5, 4, 3, 2, 1]
n=len(arr)-1
quickSort(arr, first_index=0, last_index=n)
print(arr)