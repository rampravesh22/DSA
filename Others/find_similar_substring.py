def find(input2):
    ans = []
    i = 0
    arr = input2().split(" ")
    for word in arr:
        letter = word[i]
        a = list(map(lambda y: y[i] == letter,input2))
        i += 1
        if all(a):
            ans.append(letter)
        else:
            break
    return len(ans)


n = int(input())
arr = []
for i in range(n):
    arr.append(input())
print(find(arr))
