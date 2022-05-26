"""
그리디 예제 4-3 왕실의 나이트
8 X 8 행렬에서 임의의 좌표가 주어졌을 때, (행: 1~8, 열: a~h)
나이트가 이동할 수 있는 횟수를 구하라.
단, 나이트가 이동할 때 범위를 벗어날 수 없으며
1. 수평 2칸 + 수직 1칸
2. 수직 2칸 + 수평 1칸 씩 움직일 수 있다.
"""

n = input()  # a1 형태로 현재 좌표 입력
row = int(n[1])
col = int(ord(n[0]))-96  # a의 아스키코드는 97이므로 96 씩 빼서 1로 만들어준다
count = 0

# 나이트 이동할 수 있는 경우의 수 8가지
move_types = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for i in move_types:
    if 1 <= row+i[0] <= 8 and 1 <= col+i[1] <= 8:  # 배열 범위 안이면 좌표 업데이트
        count += 1
    else:
        continue

print(count)