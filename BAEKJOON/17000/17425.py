#메모이제이션으로 1부터 1000000까지 0으로 하고, 1의 배수인 인덱스에 1을 더하고, 2의 배수인 인덱스에 2를 더하고... 를 반복해서 1, 2, 3...N의 약수의 합의 합을 구해 만들어준 뒤 원하는 값이 나오면 출력한다.

import sys
input = sys.stdin.readline

# 입력
T = int(input())

# dp 배열 초기화
dp = [0] * 1000000

# 각 쿼리에 대해 처리
for i in range(1, 1000001):
    check = 1
    while check * i <= 1000000:
        add = i * check
        dp[add - 1] += i
        check += 1

# 누적 합 계산
for k in range(1, 1000000):
    dp[k] += dp[k - 1]

# 각 쿼리에 대해 결과 출력
for _ in range(T):
    N = int(input())
    print(dp[N - 1])