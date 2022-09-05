"""
Find the non repeating character in a given string
    I/P: s = aaabccd
    O/P: b

    I/P: s = aaaacaaabbacdaddczaa
    O/P: z
"""


def non_repeating_char(s):
    freq = {}
    for each in s:        
        if each in freq.keys():
            freq[each] += 1
        else:
            freq[each] = 1
    ans = ""
    for key, value in freq.items():
        if value == 1:
            ans = key
            break
    return ans


if __name__ == "__main__":
    string_val = "aaaabaaabbaddaczaa"
    print(non_repeating_char(string_val))