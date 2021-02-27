#First Non repeating Character in a given String
'''
In Given String a = aaabccd
first Non repeating Character is b
'''
def firstNonRepeatingCharacter(s):
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

print(firstNonRepeatingCharacter("aaaabaaabbacdaddczaa"))