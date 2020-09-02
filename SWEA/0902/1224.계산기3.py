import sys
sys.stdin = open('input.txt', 'r')
def change(text):
    instack = {'(':0, '+':1, '-':1, '*':2, '/':2 }
    stack = []
    dab = ''
    for t in text:
        if t == '(':
            stack.append(t)
        elif t == '+' or t == '-' or t == '*' or t == '/':
            if instack[t] > instack[stack[-1]]:
                stack.append(t)
            else:
                while 1:
                    tmp = stack.pop()
                    dab += tmp
                    if instack[t] > instack[stack[-1]]:
                        stack.append(t)
                        break
        elif t == ')':
            while 1:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    tmp = stack.pop()
                    dab += tmp
        else:
            dab += t
    return dab

def calculate(changed):
    stack = []
    for c in changed:
        if c == '+':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a+b)
        elif c == '-':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a - b)
        elif c == '*':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a * b)
        elif c == '/':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a / b)
        else:
            stack.append(int(c))
    return stack.pop()

for tc in range(1, 11):
    length = int(input())
    text = input()
    changed = change(text)
    dab = calculate(changed)
    print('#{} {}'.format(tc, dab))


