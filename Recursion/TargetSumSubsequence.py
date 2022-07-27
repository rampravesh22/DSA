"""A subarray or substring will always be contiguous,
 but a subsequence need not be contiguous"""


def sumSubsquence(arr, len_arr, i, initial_sum, target_sum, ans=[]):
    if i == len_arr:
        if initial_sum == target_sum:
            print(ans)
            return
        return

    ans.append(arr[i])
    initial_sum += arr[i]
    sumSubsquence(arr, len_arr, i + 1, initial_sum, target_sum, ans)
    initial_sum -= arr[i]
    ans.pop()
    sumSubsquence(arr, len_arr, i + 1, initial_sum, target_sum, ans)


sumSubsquence(arr=[1, 2, 1], len_arr=3, i=0, initial_sum=0, target_sum=2)
