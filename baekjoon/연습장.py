limit = [6,4]
point = [4,1]
t = 8
new_point = []
if ((point[0] + t) //limit[0])%2 == 0:
  new_point.append((point[0] + t)%limit[0])
else:
  new_point.append(limit[0]-((point[0] + t)%limit[0]))
if ((point[1] + t) //limit[0])%2 == 0:
  new_point.append((point[1] + t)%limit[1])
else:
  new_point.append(limit[1]-((point[1] + t)%limit[1]))
print(*new_point)

if ((point[0] + t) //limit[0])%2 == 0:
  new_point.append((point[0] + t)%limit[0])
else:
  new_point.append(limit[0]-((point[0] + t)%limit[0]))
if ((point[1] + t) //limit[1])%2 == 0:
  new_point.append((point[1] + t)%limit[1])
else:
  new_point.append(limit[1]-((point[1] + t)%limit[1]))
print(*new_point)