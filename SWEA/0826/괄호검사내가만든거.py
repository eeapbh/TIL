stack = []
def check(text):
    for i in range(len(text)):

        if text[i] == '{' or text[i] == '[' or text[i] == '(':
            stack.append(text[i])
        elif text[i] == '}' or text[i] == ']' or text[i] == ')':
            if len(stack) == 0:
                return False

            temp = stack.pop()
            if text[i] == '}' and temp == '{':
                continue
            elif text[i] == ']' and temp == '[':
                continue
            elif text[i] == ')' and temp == '(':
                continue
            return False
    if len(stack) > 0:
        return False
    return True



print(check('{()}{[]}'))
print(check('([)](())'))
print(check('(][())'))