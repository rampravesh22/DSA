t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    x = int(input())
    ans = []
    for i in range(N):
        if A[i] == X:
            ans.insert(0,1)
        else:
            ans.append(A[i])

    print(*ans)