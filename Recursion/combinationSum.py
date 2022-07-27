"""A subarray or substring will always be contiguous,
 but a subsequence need not be contiguous"""


def combinationSum(arr, ind, n, target, ans, l):
    if ind == n:
        if target == 0:
            ans.append(l)

    if arr[ind] <= target:
        l.append(arr[ind])
        combinationSum(arr, ind + 1, n, target - arr[ind], ans, l)
        l.pop()
    combinationSum(arr, ind + 1, n, target, ans, l)


ans = []
l = []
combinationSum(arr=[1, 2, 3, 4, 5], ind=0, n=5, target=5, ans=ans, l=l)
print(ans)
