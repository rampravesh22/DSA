class BinarySearch:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(self.arr)

    # Find the first occurance the element in the array
    def firstOccurance(self, target):
        n = self.n
        s = 0
        e = n - 1
        occurance = -1
        while s <= e:
            mid = s + (e - s) // 2
            if target == self.arr[mid]:
                occurance = mid
                e = mid - 1
            elif target > self.arr[mid]:
                s = mid + 1
            else:
                e = mid - 1
        if occurance == -1:
            return "Element is not present in the array"
        return occurance

    # Find the first occurance the element in the array
    def lastOccurance(self, target):
        n = self.n
        s = 0
        e = n - 1
        occurance = -1
        while s <= e:
            mid = s + (e - s) // 2
            if target == self.arr[mid]:
                occurance = mid
                s = mid + 1
            elif target > self.arr[mid]:
                s = mid + 1
            else:
                e = mid - 1
        if occurance == -1:
            return "Element is not present in the array"
        return occurance

    # count element
    def countElement(self, first, last):
        return last - first + 1

    # Number of rotation
    def numberOfRotation(self, array):
        a = array
        n = len(array)
        start = 0
        end = len(array) - 1

        while start <= end:
            mid = (end - start) // 2 + start
            next = (mid + 1) % n
            prev = (mid + n - 1) % n

            if a[prev] <= a[mid] <= a[next]:
                return mid
            elif a[next] < a[mid]:
                start = mid + 1
            else:
                end = mid - 1

    # Search element from nearly sorted array
    def nearlySortedArray(self, arr, element):
        a = arr
        start = 0
        end = len(a) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if element == a[mid]:
                return mid
            elif mid - 1 >= start and a[mid - 1] == element:
                return mid - 1
            elif mid + 1 <= end and a[mid + 1] == element:
                return mid + 1

            elif element > a[mid]:
                start = mid + 1
            else:
                end = mid - 1

    # floor value in sorted array
    def floorValue(self, arr, element):
        a = arr
        start = 0
        end = len(a) - 1
        res = -1
        while start <= end:
            mid = start + (end - start) // 2

            if a[mid] == element:
                return element
            elif a[mid] < element:
                res = a[mid]
                start = mid + 1
            else:
                end = mid - 1
        if res == -1:
            return "NO"
        else:
            return res

    # Ceil value in sorted array
    def ceilValue(self, arr, element):
        a = arr
        start = 0
        end = len(a) - 1
        res = -1
        while start <= end:
            mid = start + (end - start) // 2

            if a[mid] == element:
                return element
            elif a[mid] < element:
                start = mid + 1
            else:
                res = a[mid]
                end = mid - 1
        if res == -1:
            return "NO"
        else:
            return res

    # next char in in sorted string
    def nextChar(self, arr, element):
        a = arr
        start = 0
        end = len(a) - 1
        res = -1
        while start <= end:
            mid = start + (end - start) // 2

            if a[mid] == element:
                start = mid + 1
            elif a[mid] < element:
                start = mid + 1
            else:
                res = a[mid]
                end = mid - 1
        if res == -1:
            return "NO"
        else:
            return res

    # previous character in in sorted string
    def prevChar(self, arr, element):
        a = arr
        start = 0
        end = len(a) - 1
        res = -1
        while start <= end:
            mid = start + (end - start) // 2

            if a[mid] == element:
                end = mid - 1
            elif a[mid] < element:
                res = a[mid]
                start = mid + 1
            elif a[mid] > element:
                end = mid - 1
        if res == -1:
            return "NO"
        else:
            return res

    # Search element in ifinite sorted array
    def elementInfinite(self, arr, element):
        a = arr
        start = 0
        end = 1

        while element > a[end]:
            start = end
            end = end * 2

        res = -1
        while start <= end:
            mid = start + (end - start) // 2

            if a[mid] == element:
                return mid
            elif a[mid] < element:
                start = mid + 1
            elif a[mid] > element:
                end = mid - 1
        if res == -1:
            return "NO"
        else:
            return res

    # first occurance of one in infinite array
    def firstOccuranceOf_1(self, arr, element):
        start = 0
        end = 1
        a = arr
        while element > end:
            start = end
            end = end * 2

        while start <= end:
            mid = start + (end - start) // 2

            if a[mid] == element:
                res = a[mid]
                end = mid - 1
            elif element > a[mid]:
                start = mid + 1
            elif element < a[mid]:
                end = mid - 1

    # find minimum difference with key
    def minimumDifferenceWithKey(self, arr, key):
        start = 0
        end = len(arr) - 1
        a = arr
        while start <= end:
            mid = start + (end - start) // 2

            if key == a[mid]:
                return key - a[mid]

            elif key > a[mid]:
                start = mid + 1
            elif key < a[mid]:
                end = mid - 1

        d1 = abs(a[start] - key)
        d2 = abs(a[end] - key)
        return min(d1, d2)

    # find peak element in unsorted array
    def peakElement(self, arr):
        start = 0
        end = len(arr) - 1
        n = len(arr)
        a = arr
        while start <= end:
            mid = start + (end - start) // 2

            if 0 < mid < n - 1:
                if a[mid - 1] < a[mid] and a[mid] > a[mid + 1]:
                    return mid
                elif a[mid] > a[mid - 1]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif mid == 0:
                if a[0] > a[1]:
                    return 0
                else:
                    return 1
            elif mid == n - 1:
                if a[mid] > a[mid - 1]:
                    return mid
                else:
                    return mid - 1

    # search element in two dimensional array
    def searchIn_2D_Array(self, arr, key):
        a = arr
        m = len(a)
        n = len(a[0])
        index = []
        i = 0
        j = len(arr[0]) - 1

        while 0 <= i < m and 0 <= j < n:
            if a[i][j] == key:
                index.append(i)
                index.append(j)
                break
            elif key > a[i][j]:
                i += 1
            elif key < a[i][j]:
                j -= 1
        if index:
            return index
        else:
            return -1


# first cocurance and last occurance
array = [1, 2, 3, 3, 4, 5, 5, 5, 5, 5, 5, 6, 8, 9]
b = BinarySearch(array)
first = b.firstOccurance(5)
last = b.lastOccurance(5)
print(f"First occurance: {first}")
print(f"Last occurance: {last}")

# count an element using binary search
total_count = b.countElement(first, last)
print(f"Count of element is: {total_count}")

# number of ratation of an array
rotation = b.numberOfRotation([5, 6, 7, 8, 9, 1, 2, 3, 4])
print(f"number of rotation: {rotation}")

# Serach an eleement form nearly sorted array
n_element = b.nearlySortedArray([6, 5, 3, 2, 8, 10, 9], 10)
print(f"element in nearly sorted array: {n_element}")

# floor value in sorted array
# floor value means that greatest value that is less than the element
floor_value = b.floorValue([1, 2, 6, 7, 9, 10], 2)
print(f"Floor of the element is : {floor_value}")

# ceil value in sorted array
# ceil value means that lowest value that is greater than the element
ceil_value = b.ceilValue([1, 2, 6, 7, 9, 10], 8)
print(f"ceil of the element is : {ceil_value}")

# next char in sorted string
next_char = b.nextChar('abghkm', "z")
print(f"next char in sorted string : {next_char}")

# previous character in sorted string
prev_char = b.prevChar('abghkm', "i")
print(f"previous charcater in sorted string : {prev_char}")

# find position of an element in infinite sorted array
element_infinite = b.elementInfinite([1, 2, 4, 5, 6, 7], 5)
print(f"element form infinite array : {element_infinite}")

# find minimum difference with key
min_diff = b.minimumDifferenceWithKey([1, 3, 5, 12, 34, 45], 14)
print(f"minimum differnce with key : {min_diff}")

# find peak element in unsorted array
arr = [12, 3, 5, 67, 56, 34, 2, 45]
peak_index = b.peakElement(arr)
print(f"peak_element : {arr[peak_index]}")

# search element in two dimensional array
two_D_array = [[2, 3, 4, 5, 6], [4, 5, 6, 7, 8], [10, 11, 12, 13, 14], [21, 22, 23, 24, 25, 26], [31, 32, 33, 34, 35]]
key_in_2d = b.searchIn_2D_Array(two_D_array, 13)
print(f"Element in two dimensional array index : {key_in_2d}")
