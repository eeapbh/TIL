def atoi(line):
    num = 0
    for i in range(len(line)):
        num *= 10
        num += ord(line[i]) - ord('0')

    return num
num = atoi("1234")
print(type(num), num)

def itoa(num):
    line = ''
    tmp = num
    while tmp > 0:
        number = tmp % 10
        line += chr(number+ord('0'))
        tmp //= 10

    return line
line = itoa(1234)
line2 = line[::-1]
print(type(line2), line2)