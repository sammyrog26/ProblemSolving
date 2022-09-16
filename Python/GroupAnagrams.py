"""
    Given a list of words, group the anagram in one list

    I/P:["eat", "tea", "tan", "ate", "nat", "bat"]
    O/P:[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""


def group_anagram(arr):
    if not arr:
        return
    d = {}
    for each in arr:
        sorted_val = "".join(sorted(each))
        if sorted_val not in d:
            d[sorted_val] = [each]
        else:
            d[sorted_val] += [each]
    return [d[i] for i in d]


if __name__ == "__main__":
    array = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagram(array))
