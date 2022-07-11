def poswerSet(arr, ind,ans=[]):
    if ind == len(arr):
        print(ans,end=" ")
        return
    ans.append(arr[ind])
    poswerSet(arr, ind + 1)
    ans.remove(arr[ind])
    poswerSet(arr, ind + 1)

poswerSet([3, 1, 2], 0)