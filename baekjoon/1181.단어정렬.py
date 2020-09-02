def longCheck(text):
    return len(text)

def dicCheck(text):
    a = 100**len(text)
    total = 0
    for t in text:
        total += ord(t)*a
        a /= 100
    return total

n = int(input())
texts = []
for i in range(n):
    texts.append(input())
long = sorted(texts, key=longCheck)

delete = []
for r in long:
    if r not in delete:
        delete.append(r)

result = sorted(delete, key=dicCheck)
for r in result:
    print(r)

