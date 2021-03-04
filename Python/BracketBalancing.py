def bracketBalancing(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True


print(bracketBalancing("{}[]()"))


# """
# Another Approach
# """
#
#
# def brackets(expression):
#     all_br = ['()', '{}', '[]']
#     while any(x in expression for x in all_br):
#         for br in all_br:
#             expression = expression.replace(br, '')
#             print(expression)
#     if not expression:
#         return True
#     else:
#         return False
#
# print(brackets("{}[[(())]]"))

