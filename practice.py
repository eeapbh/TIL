a = 1

def f1():
    a = 5
    f2()

def f2():

    print(a, end='')

f1()
print(a)