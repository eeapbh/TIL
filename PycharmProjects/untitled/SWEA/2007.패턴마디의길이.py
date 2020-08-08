import sys
sys.stdin = open('input.txt', 'r')
t = int(input())
for tc in range(1, t+1):
    words = input()
    j = 0
    result = 0
    for i in range(len(words)):
        r = words[:i+1]
        if r == words[i+1: i+1+len(r)]:
            result = len(r)
            break
    print(f'#{tc} {result}')