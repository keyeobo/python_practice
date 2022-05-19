"""
그리디 예제 4-1 상하좌우
여행가 A는 N X N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 x 1 크기의  정사각형으로 나누어져 있다.
가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당한다.
여행가 A는 상,하,좌,우 방향으로 이동할 수 있으며, 시작 좌표는 항상(1,1)이다.
L:왼쪽으로 한 칸 이동
R:오른쪽으로 한 칸 이동
U:위로 한 칸 이동
D:아래로 한 칸 이동
여행자 A가 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
입력 조건:
첫째 줄에 공간의 크기를 나타내는 N이 주어진다.
둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다.
출력 조건:
최종 도착할 지점의 좌표를 공백으로 구분하여 출력한다.
"""

n = int(input())
x, y = 1, 1
move = input().split()

#왼쪽, 오른쪽, 위, 아래
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for i in move:
    px = x + dx[move_types.index(i)]
    py = y + dy[move_types.index(i)]
    if 1 <= px <= n and 1 <= py <= n:  # 배열 범위 안이면 좌표 업데이트
        x = px
        y = py
    else:
        continue

print(x, y)
