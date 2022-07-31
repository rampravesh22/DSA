def is_part(list1, num):
    s = list(map(str, list1))
    s="".join(s)
    num = str(num)
    if num in s:
        return True
    return False

list1 = [2,5,3,4]
n = 5890
print(is_part(list1,n))