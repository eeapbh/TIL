n = int(input())
number = []
for i in str(n):
    number.append(i)
number.sort(reverse=True)
for i in number:
    print(i, end='')
