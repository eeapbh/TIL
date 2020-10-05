import sys
sys.stdin = open('input.txt', 'r')

limit = list(map(int, input().split()))
point = list(map(int, input().split()))
t = int(input())
new_point = []
if ((point[0] + t) //limit[0])%2 == 0:
  new_point.append((point[0] + t)%limit[0])
else:
  new_point.append(limit[0]-((point[0] + t)%limit[0]))
if ((point[1] + t) //limit[1])%2 == 0:
  new_point.append((point[1] + t)%limit[1])
else:
  new_point.append(limit[1]-((point[1] + t)%limit[1]))
print(*new_point)


