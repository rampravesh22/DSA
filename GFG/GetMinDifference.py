def getMinDiff(arr, n, k):
        arr.sort()
        ans, minimum, maximum = arr[n-1] - arr[0], arr[0], arr[n-1]
        for i in range(1,n):
            if arr[i] >= k:
                minimum, maximum = min(arr[0]+k, arr[i]-k), max(arr[i-1]+k, arr[n-1]-k)
                ans = min(ans, maximum-minimum)
        return ans


# Enter the input for this program
k = 5
n = 10
input = "2 6 3 4 7 2 10 3 2 1"
arr = input
arr=list(map(int,input.split()))
print(getMinDiff(arr, n, k))
