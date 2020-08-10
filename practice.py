a = 1
def f1():
    a = 5
    return f2
def f2():
    print(a)
print(f1())
print(a)