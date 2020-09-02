def check(text):
    for i in range(len(text)):
        if i >= 1 and text[i - 1] == text[i]:
            text.pop(i)
            text.pop(i-1)
            return check(text)
    return len(text)

t = int(input())
for tc in range(1, t+1):
    text = list(input())
    print('#{} {}'.format(tc, check(text)))


