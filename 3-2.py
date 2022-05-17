"""
그리디 예제 3-2 큰 수의 법칙
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고K가 주어질 때 큰수의 법칙에 따른 결과를 출력하시오
"""

"""
아이디어
배열 중 가장 큰 수를 k번 더한 후, 두 번째로 큰 수를 1번 더하는 것을 반복하면 가장 큰 수를 만들 수 있다. -> M//(k+1)번
나누어 떨어지지 않는 경우에는 K+1 로 나눈 나머지 만큼 가장 큰 수를 더해주면 된다. -> M%(k+1) 번
"""
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

count = int(m / (k+1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)