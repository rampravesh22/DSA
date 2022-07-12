t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    x = int(input())
    ans = []
    for i in range(n):
        if arr[i] == x:
            ans.insert(0,1)
        else:
            ans.append(arr[i])
    print(*ans)