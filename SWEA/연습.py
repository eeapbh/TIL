def solution(new_id):
    answer = ''
    for i in new_id:
        if 65 <= ord(i) <= 90:
            answer += chr(ord(i) + 32)
        if i in '-_.':
            if i == '.':
                if len(answer) == 0:
                    continue
                elif answer[-1] == '.':
                    continue
                else:
                    answer += i
            else:
                answer += i
        if 97 <= ord(i) <= 122:
            answer += i
        if i.isdigit() == 1:
            answer += i
    if answer == '':
        answer = 'a'
    while answer[-1] == '.':
        answer = answer[:len(answer) - 1]


    if len(answer) >= 16:
        answer = answer[:15]
        while answer[-1] == '.':
            answer = answer[:len(answer) - 1]

    if len(answer) <=2:
        last = answer[-1]
        while len(answer)<3:
            answer += last

    return answer


a = '=.='
print(solution(a))