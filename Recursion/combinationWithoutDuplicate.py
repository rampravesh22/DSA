# Leetcode 40 problem

def combination2(arr, n, ind, target, ds, ans):
    if target == 0:
        ans.append(ds.copy())
        return

    for i in range(ind, n):
        if i > ind and arr[i] == arr[i - 1]:
            continue
        if arr[i] > target:
            break
        ds.append(arr[i])
        combination2(arr,n,i+1, target - arr[i], ds,ans)
        ds.pop()


arr = [1, 1, 1, 2, 2]
arr.sort()
ans = []
combination2(arr,n=len(arr),ind=0,target=4,ds=[],ans=ans)
print(ans)