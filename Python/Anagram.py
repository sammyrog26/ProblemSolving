from collections import Counter


def count_anagram(s):
    if len(s) % 2 != 0:
        return -1
    else:
        s1 = Counter(s[:len(s) // 2])
        s2 = Counter(s[len(s) // 2:])
        diff = s1 - s2
        print(sum(diff.values()))


if __name__ == "__main__":
    str1 = "ababab"
    count_anagram(str1)