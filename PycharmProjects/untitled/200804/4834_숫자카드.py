t = int(input())
for i in range(1, t+1):
    len = int(input())
    number = input()
    number_li = []
    for j in number:
        number_li.append(int(j))

    results = [0]*10
    for k in range(len):
        results[number_li[k]] += 1
    for result in range(9, -1, -1):
        if results[result] == max(results):
            a = result
            break


    print(f'#{i} {a} {max(results)}')
