# 연쇄 행렬 곱셈

## 행렬의 갯수 별 경우의 수 구하기
# 3개의 행렬 => 2가지
# 4개의 행렬 => 처음 3가지 * 2가지
# 5개의 행렬 => 4 * 3 * 2
# n개의 행렬 => (n-1)!
# 결론 적으로 경우의 수는(n-1)의 팩토리얼 개이다.
import sys

R = [500] # Row
C = [500] # Colum
s = [[5,3], [3,2], [2,6]]
def MatrixMux(x, y):
    print(y)
    if y - x <= 0 : return 0;
    mm = sys.maxsize # 인트의 최대값
    for k in range(x, y-1):
        mm = min(mm, MatrixMux(x,k) + MatrixMux(k+1,y) + R[x]*C[k]*C[y])
    return mm

result = MatrixMux(0, 10)
print(result)






















