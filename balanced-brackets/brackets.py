
# less efficient implementation of same idea
def balanced_bracket(string):
    stack, brackets = [], {'}':'{', ']':'[', ')':'(', '>':'<'}
    for char in string:
        if len(stack) > 0 and char in brackets and brackets[char] == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return True if len(stack) == 0 else False

# more efficient implementation of stack solution
# same efficiency for valid bracket config
# faster at finding invalid bracket configs
def balance(string):
    stack, brackets = [], {'}':'{', ']':'[', ')':'(', '>':'<'}
    for char in string:
        if char not in brackets:
            if char in brackets.values():
                stack.append(char)
            else:
                return False
        elif len(stack) == 0 or stack[-1] != brackets[char]:
            return False
        else:
            stack.pop()
    return True # guaranteed to have empty stack at this point

a = ")([][[])" #invalid
b = "[}()[]<>" #invalid
c = "99<>()" #invalid
d = "[](<<[]>()>)" #valid
