# w로 시작하는 체스판이랑 B로 시작하는 체스판만들기
# 파리채마냥 8x8씩 확인 다를때마다 cnt+= 1해서 어디에 저장
# 젤작은거 출력
import sys
sys.stdin = open('input.txt', 'r')

def check(arr):
    cnt_W = 0
    cnt_B = 0

    for i in range(8):
        for j in range(8):
            if arr[i][j] != start_B[i][j]:
                cnt_B +=1
            if arr[i][j] != start_W[i][j]:
                cnt_W += 1
    result.append(min(cnt_B, cnt_W))

M, N = map(int, input().split())
chess = [list(input()) for _ in range(M)]
start_W = [
    ['W', 'B','W', 'B','W', 'B','W', 'B'],
    ['B','W', 'B','W', 'B','W', 'B','W'],
    ['W', 'B','W', 'B','W', 'B','W', 'B'],
    ['B','W', 'B','W', 'B','W', 'B','W'],
    ['W', 'B','W', 'B','W', 'B','W', 'B'],
    ['B','W', 'B','W', 'B','W', 'B','W'],
    ['W', 'B','W', 'B','W', 'B','W', 'B'],
    ['B','W', 'B','W', 'B','W', 'B','W']
]
start_B = [
    ['B','W', 'B','W', 'B','W', 'B','W'],
    ['W', 'B','W', 'B','W', 'B','W', 'B'],
    ['B','W', 'B','W', 'B','W', 'B','W'],
    ['W', 'B','W', 'B','W', 'B','W', 'B'],
    ['B','W', 'B','W', 'B','W', 'B','W'],
    ['W', 'B','W', 'B','W', 'B','W', 'B'],
    ['B','W', 'B','W', 'B','W', 'B','W'],
    ['W', 'B','W', 'B','W', 'B','W', 'B']
]
arr = [['']*8 for _ in range(8)]
result = []
for i in range(M-8+1):
    for j in range(N-8+1):
        for a in range(8):
            for b in range(8):
                arr[a][b] = chess[i+a][j+b]
        check(arr)
print(min(result))