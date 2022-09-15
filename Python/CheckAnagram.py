"""
Check if the given two words are Anagram
eg:
    I/P: LISTEN SILENT
    O/P: True

    I/P: Horse House
    O/P: False

    I/P: Horsss Horses
    O/P: False
"""


def check_anagram(first, second):

    first = [each for each in first]
    second = [each for each in second]
    for each_char in first:
        if each_char in second:
            second.remove(each_char)
    if len(second) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    v1 = "listen"
    v2 = "silent"
    print(check_anagram(v1, v2))
