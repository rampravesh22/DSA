def poswerSet(arr, ind,ans=[]):
    if ind == len(arr):
        print(ans,end=" ")
        return
    # take condition
    ans.append(arr[ind])
    poswerSet(arr, ind + 1)
    ans.pop()
    # not take condtion
    poswerSet(arr, ind + 1)
print("powerset = {",end=" ")
poswerSet([3, 1, 2], 0)
print("}")
