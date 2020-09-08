import socket
import time
import math

# User and Launcher Information
NICKNAME = 'DAEJEON02_LEEHYUNWOO'
HOST = '127.0.0.1'

# Static Value(Do not modify)
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# Predefined Variables(Do not modify)
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]


class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: %s:%d' % (HOST, PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: %s:%d' % (HOST, PORT))
        send_data = '%d/%s/' % (CODE_SEND, NICKNAME)
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play!\n--------------------')

    def request(self):
        self.sock.send('%d/%d' % (CODE_REQUEST, CODE_REQUEST).encode())
        print('Received Data has been currupted, Resend Requested.')

    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: %s' % recv_data)
        return recv_data

    def send(self, angle, power):
        if power <= 0:
            print('Power must be bigger than 0, Try again.')
            return False
        merged_data = '%f/%f/' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: %s' % merged_data)

    def close(self):
        self.sock.close()
        print('Connection Closed.\n--------------------')


class GameData:
    def __init__(self):
        self.order = 0
        self.reset()

    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)

    def arrange(self):
        self.order = self.balls[0][1]
        print('\n* You will be the %s player. *\n' %
              ('first' if self.order == 1 else 'second'))

    def show(self):
        print('====== Arrays ======')
        for i in range(NUMBER_OF_BALLS):
            print('Ball %d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print('====================')

# 각도계산 함수
def degree(white, obj):
    # white : 흰공, obj : 목적구를 치기위한 위치
    # 사인함수
    # 빗변
    hypo = ((obj[0] - white[0]) ** 2 + (obj[1] - white[1]) ** 2) ** (1 / 2)
    # 높이
    height = abs(obj[1] - white[1])

    # 오른쪽 위
    if obj[0] - white[0] > 0 and obj[1] - white[1] > 0:
        # 사인값을 역함수를 통해 구하려는 각도의 라디안값을 구함
        y = math.asin(height / hypo)
        # 라디안 -> 각도
        return 90 - math.degrees(y)
    # 왼쪽 위
    elif obj[0] - white[0] < 0 and obj[1] - white[1] > 0:
        # 사인값을 역함수를 통해 구하려는 각도의 라디안값을 구함
        y = math.asin(height / hypo)
        # 라디안 -> 각도
        return 270 + math.degrees(y)
    # 왼쪽 아래
    elif obj[0] - white[0] < 0 and obj[1] - white[1] < 0:
        # 사인값을 역함수를 통해 구하려는 각도의 라디안값을 구함
        y = math.asin(height / hypo)
        # 라디안 -> 각도
        return 270 - math.degrees(y)
    # 오른쪽 아래
    elif obj[0] - white[0] > 0 and obj[1] - white[1] < 0:
        # 사인값을 역함수를 통해 구하려는 각도의 라디안값을 구함
        y = math.asin(height / hypo)
        # 라디안 -> 각도
        return 90 + math.degrees(y)
    elif obj[0] - white[0] == 0 and obj[1] - white[1] < 0:
        return 0
    elif obj[0] - white[0] > 0 and obj[1] - white[1] == 0:
        return 90
    elif obj[0] - white[0] == 0 and obj[1] - white[1] > 0:
        return 180
    elif obj[0] - white[0] < 0 and obj[1] - white[1] == 0:
        return 270

# 쳐야될 위치의 x좌표를 구하는 함수
def locx(loc, hole):
    # loc : 목적구, hole : 구멍
    # hole이 왼쪽에 있을 경우
    if loc[0] - hole[0] > 0:
        return loc[0] + abs(((5.72*(loc[0]-hole[0]))/(((hole[0]-loc[0])**2 + (hole[1] -loc[1])**2)**(1/2))))
    # hole이 오른쪽에 있을 경우
    elif loc[0] - hole[0] < 0:
        return loc[0] - abs(((5.72*(loc[0]-hole[0]))/(((hole[0]-loc[0])**2 + (hole[1] -loc[1])**2)**(1/2))))
# 쳐야될 위치의 y좌표를 구하는 함수
def locy(loc, hole):
    # hole이 더 위에 있을 경우
    if loc[1] - hole[1] < 0:
        return loc[1] - abs(((5.72*(loc[1]-hole[1]))/(((hole[0]-loc[0])**2 + (hole[1] -loc[1])**2)**(1/2))))
    # hole이 더 아래에 있을 경우
    elif loc[1] - hole[1] > 0:
        return loc[1] + abs(((5.72*(loc[1]-hole[1]))/(((hole[0]-loc[0])**2 + (hole[1] -loc[1])**2)**(1/2))))
# 쿠션으로 칠때 어느곳을 쳐야하는지 고르기
def top_middle(white, obj):
    z = (obj[0] - white[0]) * ((white[1]) / (white[1]+obj[1]))
    return (white[0]+abs(z), 127)

def bottom_middle(white, obj):
    z = (obj[0] - white[0]) * ((white[1]) / (white[1]+obj[1]))
    return (white[0]+abs(z), 0)

def play(conn, gameData):
    # angle = 0.0
    # power = 0.0
    ##############################
    # Begining of Your Code
    # Put your code here to set angle and power values.
    # angle(float) must be between 0.0 and 360.0
    # power(float) must be between 0.0 and 100.0
    # 선공일 때

    # 후공일 때
    if gameData.order == 1:
        # 2,4번 공이 없으면 8번공을 치겠다.
        if gameData.balls[2] == [-1, -1] and gameData.balls[4] == [-1, -1] and gameData.balls[5] != [-1, -1]:
            total = []
            result = []
            for i in range(6):
                total.append(abs((degree(gameData.balls[0], HOLES[i]) - degree(gameData.balls[5], HOLES[i]))))
                result.append(((HOLES[i][0] - gameData.balls[5][0]) ** 2 + (HOLES[i][1] - gameData.balls[5][1]) ** 2) ** (1 / 2))
            if result.index(min(result)) == total.index(min(total)):
                arr3 = HOLES[total.index(min(total))]
            elif result.index(min(result)) != total.index(min(total)):
                arr3 = HOLES[result.index(min(result))]
            location = (locx(gameData.balls[5], arr3), locy(gameData.balls[5], arr3))

        # 2번 공이 없으면 4번공을 치겠다.
        elif gameData.balls[2] == [-1, -1] and gameData.balls[4] != [-1, -1]:
            total = []
            result = []
            for i in range(6):
                total.append(abs((degree(gameData.balls[0], HOLES[i]) - degree(gameData.balls[4], HOLES[i]))))
                result.append(((HOLES[i][0] - gameData.balls[4][0]) ** 2 + (HOLES[i][1] - gameData.balls[4][1]) ** 2) ** (1 / 2))
            if result.index(min(result)) == total.index(min(total)):
                arr2 = HOLES[total.index(min(total))]
            elif result.index(min(result)) != total.index(min(total)):
                arr2 = HOLES[result.index(min(result))]

            location = (locx(gameData.balls[4], arr2), locy(gameData.balls[4], arr2))

        # 2번 공이 있으면 2번공을 치겠다.
        elif gameData.balls[2] != [-1, -1]:
            total = []
            result = []
            for i in range(6):
                total.append(abs((degree(gameData.balls[0], HOLES[i]) - degree(gameData.balls[2], HOLES[i]))))
                result.append(((HOLES[i][0] - gameData.balls[2][0]) ** 2 + (HOLES[i][1] - gameData.balls[2][1]) ** 2) ** (1 / 2))
            if result.index(min(result)) == total.index(min(total)):
                arr1 = HOLES[total.index(min(total))]
            elif result.index(min(result)) != total.index(min(total)):
                arr1 = HOLES[result.index(min(result))]
            location = (locx(gameData.balls[2], arr1), locy(gameData.balls[2], arr1))
            angle = degree(gameData.balls[0], location)
            whiteBall_x = gameData.balls[0][0]
            whiteBall_y = gameData.balls[0][1]
            width = abs(location[0] - whiteBall_x)
            height = abs(location[1] - whiteBall_y)
            distance = (math.sqrt(width ** 2 + height ** 2)) / 3
        power = distance

    else:
        cnt = 0
        # 1,3번 공이 없으면 8번공을 치겠다.
        if cnt == 0:
            cnt += 1
            angle = 90
            distance = (((gameData.balls[0][0] - gameData.balls[1][0])**2 + (gameData.balls[0][1] - gameData.balls[1][1])**2)**(1/2)) / 6
        else:
            if gameData.balls[1] == [-1, -1] and gameData.balls[3] == [-1, -1] and gameData.balls[5] != [-1, -1]:
                total = []
                result = []
                for i in range(6):
                    total.append(abs((degree(gameData.balls[0], HOLES[i]) - degree(gameData.balls[5], HOLES[i]))))
                    result.append(((HOLES[i][0] - gameData.balls[5][0]) ** 2 + (HOLES[i][1] - gameData.balls[5][1]) ** 2) ** (1 / 2))
                # 각의 차이가 제일 작고, ball과의 거리가 가까운 홀을 택하겠다.
                if result.index(min(result)) == total.index(min(total)):
                    arr3 = HOLES[total.index(min(total))]
                elif result.index(min(result)) != total.index(min(total)):
                    arr3 = HOLES[result.index(min(result))]
                location = (locx(gameData.balls[5], arr3), locy(gameData.balls[5], arr3))

            # 1번 공이 없으면 3번공을 치겠다.
            elif gameData.balls[1] == [-1, -1] and gameData.balls[3] != [-1, -1]:
                total = []
                result = []
                for i in range(6):
                    total.append(abs((degree(gameData.balls[0], HOLES[i]) - degree(gameData.balls[3], HOLES[i]))))
                    result.append(((HOLES[i][0] - gameData.balls[3][0]) ** 2 + (HOLES[i][1] - gameData.balls[3][1]) ** 2) ** (1 / 2))
                if result.index(min(result)) == total.index(min(total)):
                    arr2 = HOLES[total.index(min(total))]
                elif result.index(min(result)) != total.index(min(total)):
                    arr2 = HOLES[result.index(min(result))]
                location = (locx(gameData.balls[3], arr2), locy(gameData.balls[3], arr2))

            # 1번 공이 있으면 1번공을 치겠다.
            elif gameData.balls[1] != [-1, -1]:
                total = []
                result = []
                for i in range(6):
                    total.append(abs((degree(gameData.balls[0], HOLES[i]) - degree(gameData.balls[1], HOLES[i]))))
                    result.append(((HOLES[i][0] - gameData.balls[1][0]) ** 2 + (HOLES[i][1] - gameData.balls[1][1]) ** 2) ** (1 / 2))
                if result.index(min(result)) == total.index(min(total)):
                    arr1 = HOLES[total.index(min(total))]
                elif result.index(min(result)) != total.index(min(total)):
                    arr1 = HOLES[result.index(min(result))]
                location = (locx(gameData.balls[1], arr1), locy(gameData.balls[1], arr1))


            angle = degree(gameData.balls[0], location)
            whiteBall_x = gameData.balls[0][0]
            whiteBall_y = gameData.balls[0][1]
            width = abs(location[0] - whiteBall_x)
            height = abs(location[1] - whiteBall_y)
            distance = (math.sqrt(width ** 2 + height ** 2)) / 3
        power = distance




    # radian = math.atan(width / height)
    # targetBall_x = gameData.balls[1][0]
    # targetBall_y = gameData.balls[1][1]
    # angle = 180 / math.pi * radian
    # power = distance
    # You can clear Stage 1 with the pre-written code above.
    # Those will help you to figure out how to clear other Stages.
    # Good luck!!
    # End of Your Code
    ##############################

    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        if gameData.balls[0][0] == SIGNAL_ORDER:
            gameData.arrange()
            continue
        elif gameData.balls[0][0] == SIGNAL_CLOSE:
            break
        gameData.show()
        play(conn, gameData)
    conn.close()


if __name__ == '__main__':
    main()

