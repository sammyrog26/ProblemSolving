"""
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length
    and answer[i] is the distance from index i to the closest occurrence of character c in s.

    Input: s = "loveleetcode", c = "e"
    Output: [3,2,1,0,1,0,0,1,2,2,1,0]
    Explanation:
        The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
        The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
        The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
        For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
        The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

    Input: s = "aaab", c = "b"
    Output: [3,2,1,0]
"""


def shortest_to_char(s, c):
    ans = [0 if s[0] == c else 10001]
    for i in range(1, len(s)):
        ans.append(0 if s[i] == c else ans[i - 1] + 1)
    for i in range(len(s) - 2, -1, -1):
        ans[i] = min(ans[i], ans[i + 1] + 1)
    return ans


if __name__ == "__main__":
    str_val = "loveleetcode"
    char = "e"
    print(shortest_to_char(str_val, char))
