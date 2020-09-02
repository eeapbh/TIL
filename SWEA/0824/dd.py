#1.
#int형을 문자열로 전환
def itoa(num):
    line = ''
    tmp = num
    while tmp >0:
        number = tmp % 10
        #0을 아스키코드값으로 바꾼 것을 더하면 지금 숫자의 아스키코드값을 알 수 있음
        #다음값을 이전 문자 앞에 더해줘도 되고, 다 만든 뒤 아까 배운 문자 뒤집기해도딤
        line = chr(number+ord('0')) + line
        tmp //= 10
    return line
line = itoa(1234)
print(type(line),line)

