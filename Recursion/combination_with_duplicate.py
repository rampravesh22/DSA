"""A subarray or substring will always be contiguous,
 but a subsequence need not be contiguous"""
# LeetCode 39

def combinationSum(arr, ind, n, target, ans, l):
    if ind == n:
        if target == 0:
            ans.append(l.copy())
        return None
    if target >= arr[ind]:
        l.append(arr[ind])
        combinationSum(arr, ind, n, target - arr[ind], ans, l)
        l.pop()
    combinationSum(arr, ind + 1, n, target, ans, l)


ans = []
l = []
arr = [2, 3, 6, 7]
ind = 0
target = 7
n = len(arr)
combinationSum(arr, ind, n, target, ans, l)
print(ans)
