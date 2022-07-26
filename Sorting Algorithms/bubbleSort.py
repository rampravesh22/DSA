# l = list(map(int, input('Enter the number to sort: ').split()))
l = [45, 0, 5, 3, 1]
n = len(l)
for i in range(n - 1):
    print(f"({i + 1})- iteration: ")

    for j in range(n - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
            print(f"{j + 1}- swap {l[j]} and {l[j + 1]}: ", end="")
            print(*l)
        else:
            print(f'{j + 1}- No swap     : ', end="")
            print(*l)
    print()
print(f"Sorted list: {l}")
