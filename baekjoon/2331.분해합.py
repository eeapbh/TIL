target = int(input())
number = 0
while number < 1000000:
    number += 1
    change = []
    change = list(map(int, str(number)))
    if target == sum(change) + number:
        result = number
        break
    result = 0
print(result)
