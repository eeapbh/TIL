import sys
sys.stdin = open('input.txt', 'r')

def calculate(text):
    stack = []
    for t in text:
        if t in '*/+-': # 연산자면
            if len(stack)>1:# stack에 값이 2개이상 있으면
                b = int(stack.pop())
                a = int(stack.pop())
                if t == '*':
                    stack.append(int(a * b))
                if t == '/':
                    stack.append(int(a / b))
                if t == '+':
                    stack.append(int(a + b))
                if t == '-':
                    stack.append(int(a - b))
            else:# stack에 값이 2개이상 없으면 pop이 안되니까 에러
                return 'error'

        elif t == '.':
            if text.index(t) == len(text) - 1: # 지금 포문이 끝까지돌았는데 하나 있다는거는 계산이 다된것이니 최종계산값 pop
                if len(stack) == 1: # stack에 값이 하나있으면 pop
                    return stack.pop()
                else: # 아니면 error
                    return 'error'
            else:
                return 'error'


        else: # 숫자는 stack에 append
            stack.append(t)


t = int(input())
for tc in range(1, t+1):
    text = input().split()
    print('#{} {}'.format(tc, calculate(text)))


