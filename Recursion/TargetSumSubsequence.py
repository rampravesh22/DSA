def sumSubsquence(arr, len_arr, i, initial_sum, target_sum, ans=[]):
    if i == len_arr:
        if initial_sum == target_sum:
            print(ans)

    ans.append(arr[i])
    initial_sum += arr[i]
    sumSubsquence(arr, i + 1, initial_sum, target_sum, ans)
    initial_sum -= arr[i]
    ans.remove(arr[i])
    sumSubsquence(arr, i + 1, initial_sum, target_sum, ans)

print(sumSubsquence([1, 2, 1], 3, 0, 0, 2))
