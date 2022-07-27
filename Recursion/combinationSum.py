"""A subarray or substring will always be contiguous,
 but a subsequence need not be contiguous"""


def combinationSum(arr, ind, n, target, ans, l):
    if ind == n:
        if target == 0:
            ans.append(l)
        return
    if arr[ind] <= target:
        l.append(arr[ind])
        combinationSum(arr, ind, n, target - arr[ind], ans, l)
        l.pop()
    combinationSum(arr, ind + 1, n, target, ans, l)


ans = []
l = []
arr = [1, 2, 3, 4, 5]
ind = 0
target = 5
n = len(arr)
x=combinationSum(arr, ind, n, target, ans, l)
print(ans)
print(x)
