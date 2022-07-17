def sumSubsquence(arr, len_arr, i, initial_sum, target_sum, ans=[]):
    if i == len_arr:
        if initial_sum == target_sum:
            return ans
        return False
    ans.append(arr[i])
    initial_sum += arr[i]
    if (sumSubsquence(arr, len_arr, i + 1, initial_sum, target_sum, ans)):
        return ans
    initial_sum -= arr[i]
    ans.remove(arr[i])
    if (sumSubsquence(arr, len_arr, i + 1, initial_sum, target_sum, ans)):
        return ans
    return False

ans = sumSubsquence([1, 3, 2, 5, 7], 5, 0, 0, 7)
if ans:
    print(ans)
else:
    print("Target sum subsequence is not exist")
