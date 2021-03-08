"""
Find position of substring in a given string.

Example:
    String = "aaabcnasodnoajsdabcosadj"
    needle = "abc"
            aaabcnasodnoajsdabcosadj
              ^             ^
"""


def compareString(needle, haystack, p):
    p2 = 0
    while p2 < len(needle):
        if needle[p2] != haystack[p]:
            return False
        p2 += 1
        p += 1
    return True


def needle_haystack(haystack, needle):
    if len(needle) == 0 or len(needle) > len(haystack):
        return None
    result = []
    p = 0
    while p < len(haystack) - len(needle) + 1:
        if haystack[p] == needle[0]:
            if compareString(needle, haystack, p):
                result.append(p)
        p += 1
    return result


if __name__ == "__main__":
    print(needle_haystack("bbbbbbb", "b"))
    print(needle_haystack("abcnchrabc", "abc"))
