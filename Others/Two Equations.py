x = 6
y = 4
a=0
b=0
ans = []
while a<=max(x,y) and b<=max(x,y):
    if a+b == x and a ^ b==y:
        ans.append([a,b])
print()
