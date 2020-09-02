def f(text):
    stack = []
    for i in range(len(text)):
        if text[i] == '{' or text[i] == '[' or text[i] == '(':
            stack.append(text[i])
        elif text[i] == '}' or text[i] == ']' or text[i] == ')':
            if len(stack) == 0:
                return 0
            else:
                tmp = stack.pop()
                if tmp == '{' and text[i] == '}':
                    continue
                if tmp == '[' and text[i] == ']':
                    continue
                if tmp == '(' and text[i] == ')':
                    continue
                return 0
    if len(stack) > 0:
        return 0
    return 1

t = int(input())
for tc in range(1, t+1):
    text = input()
    print('#{} {}'.format(tc, f(text)))