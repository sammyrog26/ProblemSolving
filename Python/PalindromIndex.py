"""
    Given a string of lowercase letters in the range ascii[a-z],
    determine the index of a character that can be removed to make the string a palindrome.
    There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution,
    return -1. Otherwise, return the index of a character to remove.

    I/P: aaab
    O/P: 3

    I/P: baa
    O/P: 0

    I/P: aaa
    O/P: -1

"""


def palindrome_index(s):
    l = len(s)
    index = 0
    reverse_index = l - 1
    while index < l:
        if s[index] != s[reverse_index]:
            break
        index += 1
        reverse_index -= 1

    if index > reverse_index:
        return -1
    a = index + 1
    b = reverse_index

    while a < reverse_index and b > index + 1:
        if s[a] != s[b]:
            return reverse_index
        a += 1
        b -= 1
    return index


if __name__ == "__main__":
    str_val = "aaab"
    print(palindrome_index(str_val))