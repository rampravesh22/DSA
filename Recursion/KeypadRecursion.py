def keypadRecursion(digit_str, output_str, index, ans_list, digits_mapping):
    if index == len(digit_str):
        x = "".join(output_str)
        ans_list.append(x)
        return
    curr_digit = int(digit_str[index])
    letter_string_of_digit = digits_mapping[curr_digit]
    for i in range(len(letter_string_of_digit)):
        output_str.append(letter_string_of_digit[i])
        keypadRecursion(digit_str, output_str, index + 1, ans_list, digits_mapping)
        output_str.pop()


ans = []
digits = "23"
if len(digits) == 0:
    print(ans)
output_str = ""
ind = 0
digits_mapping = {
    0: "",
    1: "",
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}
keypadRecursion(digits, [], ind, ans, digits_mapping)
print(ans)
