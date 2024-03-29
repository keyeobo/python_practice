"""
그리디 예제 3-4 1이 될 때까지
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
N을 1로 만드는 최소 횟수를 출력하시오.
"""

"""
아이디어
최대한 많이 나눈다.
N이 K의 배수가 될 때까지 1씩 빼준다.
"""

n, k = map(int, input().split())
count = 0

while True:
    if n < k:  # n이 k로 나눌 수 없을 때 break
        break
    if n % k == 0:  # n이 k의 배수면 조건2 실행
        n = n // k
        count += 1
    else:  # n이 K의 배수가 아니면, 배수가 될 때 까지 조건1 실행
        n -= 1
        count += 1

print(count)
