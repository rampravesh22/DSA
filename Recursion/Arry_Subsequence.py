def poswerSet(arr, ind,ans=[]):
    if ind == len(arr):
        print(ans,end=" ")
        return

    # take condition
    ans.append(arr[ind])
    poswerSet(arr, ind + 1)
    ans.remove(arr[ind])
    # not take condtion
    poswerSet(arr, ind + 1)
poswerSet([3, 1, 2], 0)