def count(n):
    total = 0
    for num in range(1,n+1):
        x=str(num)
        if len(x)%2!=0:
            total+=1

    return total
s=count(786)
print(s)
