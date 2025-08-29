from collections import deque

N, K = map(int, input().split())
belt = list(map(int, input().split()))
belt = deque(belt)
robot = [0] * N
robot = deque(robot)
up = 0
down = N - 1
stage = 1
while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한칸 회전
    last_belt = belt.pop()
    belt.appendleft(last_belt)
    last_robot = robot.pop()
    robot.appendleft(last_robot)

    # 마지막 칸 확인
    if robot[-1] == 1:
        robot[-1] = 0

    # 2. 가장 먼저 벨트에 올라간 로봇부터 한 칸 이동 가능하면 이동
    for idx in range(N - 2, -1, -1):
        if robot[idx] == 1 and robot[idx + 1] == 0 and belt[idx + 1] != 0:
            robot[idx + 1] = 1
            belt[idx + 1] -= 1
            robot[idx] = 0

    # 마지막 칸 확인
    if robot[-1] == 1:
        robot[-1] = 0
    
    # 첫번째 칸 놓기
    if belt[0] >= 1:
        belt[0] -= 1
        robot[0] = 1
    
    if belt.count(0) >= K:
        break
    else:
        stage += 1
print(stage)