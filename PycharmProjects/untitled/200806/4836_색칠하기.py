import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    arrs = [[''] * 10 for _ in range(10)]
    x1s, x2s, y1s, y2s, colors = [], [], [], [], []
    count = 0
    N = int(input())
    for _ in range(N):
        x1, y1, x2, y2, c = map(int, input().split())
        x1s.append(x1)
        x2s.append(x2)
        y1s.append(y1)
        y2s.append(y2)
        colors.append(c)
        # colors리스트를 만들어서 c를 저장 빨강은 1 파랑은 2
        # colors리스트를 돌리면서 c가 1인거 쭉돌리면서 1을 더함 이미 0인것만
        # c가 2이면 1을 더하는데 이미 1인거만 1을 더함
        # 최종으로 2인거의 갯수를 구함
    for n in range(N):
        if colors[n] == 1:
            for i in range(x1s[n], x2s[n]+1):
                for j in range(y1s[n], y2s[n]+1):
                    arrs[i][j] += 'r'
        else:
            for i in range(x1s[n], x2s[n]+1):
                for j in range(y1s[n], y2s[n]+1):
                    arrs[i][j] += 'b'
    for arr in arrs:
            for result in arr:
                if 'r' in result:
                    if 'b' in result:
                        count += 1
    print(f'#{tc} {count}')