"""
This functions swaps the Cases and prints the words in revers swap order
eg:
best am i-----> I AM BEST
Best am I-----> i am bEST
Love IS GamIng ------> gAMiNG is lOVE
"""


def reverse_words_order_and_swap_cases(sentence):
    swap = sentence.swapcase()
    print("Swapcase", swap)
    newlist = list(swap.split())
    string = ''
    for i in range(len(newlist) - 1, -1, -1):
        print("I>>>>>>> ", i)
        string = string + newlist[i] + " "
    return string


print(reverse_words_order_and_swap_cases("best am i"))
