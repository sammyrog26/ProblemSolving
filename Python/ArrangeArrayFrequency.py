"""
Arrange a list based on their frequency in descending order
eg:
    I/P: [5, 4, 3, 5, 3, 5]
    O/P: [5, 5, 5, 3, 3, 4]

    I/P: [5, 4, 3, 4, 3, 5, 5]
    O/P: [5, 5, 5, 3, 3, 4, 4]
"""


def compare(t1, t2):
    if t1[1] == t2[1]:
        if t1[0] < t2[0]:
            return t1[0], t2[0], t1[1]
        else:
            return t2[0], t1[0], t1[1]
    else:
        return t1[0], 0, t1[1]


def arrange_list(arr):
    if not arr:
        return
    result = []
    d = {}
    for each in arr:
        if each not in d:
            d[each] = 1
        else:
            d[each] += 1
    sorted_value_key_pairs = sorted(d.items(), key=lambda val: val[1], reverse=True)

    # Bubble Sort
    for i, each in enumerate(sorted_value_key_pairs):
        for j, each_val in enumerate(sorted_value_key_pairs):
            if each == each_val:
                continue
            elif each[1] == each_val[1]:
                if each[0] < each_val[0]:
                    temp = sorted_value_key_pairs[i]
                    sorted_value_key_pairs[i] = sorted_value_key_pairs[j]
                    sorted_value_key_pairs[j] = temp

    for final_tup in sorted_value_key_pairs:
        for i in range(final_tup[1]):
            result.append(final_tup[0])

    return result


if __name__ == "__main__":
    l = [5, 4, 3, 5, 3, 5]
    print(arrange_list(l))
