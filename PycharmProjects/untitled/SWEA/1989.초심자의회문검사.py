import sys
sys.stdin = open('input.txt', 'r')
t = int(input())
word = ''
for tc in range(1, t+1):
    word = input()
    j = 0
    for i in range(len(word)//2):
        j += 1
        if word[i] != word[len(word)-j]:
            result = 0
            break
        result = 1
    print(f'#{tc} {result}')