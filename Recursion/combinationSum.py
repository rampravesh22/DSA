def combinationSum(arr, i, n, target, ans=[]):
    if i == n:
        if sum(ans) == target:
            print(ans)
            return

    ans.append(arr[i])
    combinationSum(arr, i + 1, n, target, ans)
    ans.pop()
    combinationSum(arr, i + 1, n, target, ans)

combinationSum([1,2,3,4,5],0,5,5)
