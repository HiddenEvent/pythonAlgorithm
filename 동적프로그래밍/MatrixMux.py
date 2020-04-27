# 연쇄 행렬 곱셈

## 행렬의 갯수 별 경우의 수 구하기 => (n-1)의 팩토리얼
# 3개의 행렬 => 2가지
# 4개의 행렬 => 처음 3가지 * 2가지
# 5개의 행렬 => 4 * 3 * 2
# n개의 행렬 => (n-1)!
# 결론 적으로 경우의 수는(n-1)의 팩토리얼 개이다.
import sys
N = 4
d = [10, 30, 5, 60]
M = [[0 for x in range(N)] for y in range(N)]

for diag in range(1, N):
    for i in range(1, N - diag):
        j = i + diag
        M[i][j] = sys.maxsize
        for k in range(i, j):
            M[i][j] = min(M[i][j],
                          M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j])

print(M[1][N-1])






















