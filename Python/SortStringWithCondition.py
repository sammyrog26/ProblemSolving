"""

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

    I/P: Sorting1234
    O/P: ginortS1324
"""


def sort_with_condition(str_val):
    """
    Method 1
    """
    sorted_list = sorted([x for x in str_val])
    l = []
    for each in sorted_list:
        if each.islower():
            l.append(each)

    for each in sorted_list:
        if each.isupper():
            l.append(each)

    for each in sorted_list:
        if each.isnumeric():
            if int(each) % 2 != 0:
                l.append(each)

    for each in sorted_list:
        if each.isdigit():
            if int(each) % 2 == 0:
                l.append(each)

    print("".join(l))


def sort_with_condition2(str_val):
    """
    Method 2
    """
    s = sorted(str_val, key=lambda x: (not x.islower(), not x.isupper(), not x.isdigit(), not int(x) % 2 if x.isdigit() else 2, x))
    print(s)


if __name__ == "__main__":
    string_val = "Sorting1324"
    sort_with_condition(string_val)
    # sort_with_condition2(string_val)