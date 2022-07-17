def countSubWithTargetSum(arr, i, target_sum, ans=[], count=0):
    if i == len(arr):
        if sum(ans) == target_sum:
            return 1
        return 0

    ans.append(arr[i])
    l = countSubWithTargetSum(arr, i + 1, target_sum, ans, count)
    ans.pop()
    r = countSubWithTargetSum(arr, i + 1, target_sum, ans, count)
    return l + r

print(countSubWithTargetSum(arr=[1, 2, 3, 1, 1], i=0, target_sum=2))
