import math
holes = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
balls = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
balls[0][0], balls[0][1] = 40, 70
white = 0, 0
target1 = (1, 3**(1/2))
target2 = (3**(1/2), -1)
target3 = (-1, -(3**(1/2)))
target4 = (-1, 3**(1/2))
target5 = (1, 1)
# a 흰공
# b 목적구
def getAngle(target, white):
    # ++
    # +-
    # --
    # -+
    dx = abs(target[0] - white[0])
    dy = abs(target[1] - white[1])
    slide = ((dx**2) + (dy**2))**(1/2)
    if target[0]-white[0]>0 and target[1]-white[1]>0:
        radian = math.asin(dx/slide)
        return math.degrees(radian)

    elif target[0]-white[0]>0 and target[1]-white[1]<0:
        radian = math.asin(dy/slide)
        return math.degrees(radian)+90

    elif target[0]-white[0]<0 and target[1]-white[1]<0:
        radian = math.asin(dx/slide)
        return math.degrees(radian)+180

    elif target[0]-white[0]<0 and target[1]-white[1]>0:
        radian = math.asin(dy / slide)
        return math.degrees(radian)+270


result = getAngle(target2, white)
print(result)



