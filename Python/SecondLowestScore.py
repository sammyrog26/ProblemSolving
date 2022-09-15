"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s)
    of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name
    on a new line.

eg:
    I/P: [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    O/P: Berry
         Harry
"""


def find_lowest_second_lowest(arr):
    if not arr:
        return
    score = sorted(set(i[1] for i in arr))[1]
    low = [x[0] for x in arr if x[1] == score]
    low.sort()
    for p in low:
        print(p)


if __name__ == "__main__":
    l = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    find_lowest_second_lowest(l)