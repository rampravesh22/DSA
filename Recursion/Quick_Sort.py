"""
Quick sort algorithm:
    1.Also called as partition exchange sort.
    2.Deveploped by tony hoare in 1959 and published in 1961
    3.When implemented well it can be about 2 or 3 times faster than
      its main competitors merge sort and heap sort.

(a). For ascending order : <smaller value>  <pivot>  <bigger value>
(b). For descending order : <bigger value>  <pivot>  <smaller value>

Pivot element can be :
    1. First element.
    2. Last element.
    3. Any random element.
    4. Median of three value (first, middle, last)

Alorithms for sorting : It is for dry run =>
    arr = [14,25,100,14,1,17]
    left = 0
    right = 4  { len(arr)-2 }
    pivot = 5  { len(arr)-1 }
    while left <= right:
        if arr[left] <= pivot:
            left = left + 1
        else:
            break

    while left <= right:
        if arr[right] > = pivot:
            right = right - 1
        else:
            break



"""
