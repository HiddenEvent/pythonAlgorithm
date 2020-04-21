# 좌표평명 두 점 사이의 거리 구하는 알고리즘
# 좌표평면 = x축, y축
# x축은 가로
# y축은 세로
# (1,2) -> (3,4) 거리를 구해보자.
# 1)  (0,0) 에서 부터 시작해보자
import math

A = (0, 0)
B = (2, 2, 1, 2)

def getDistance(coordinates_A, coordinates_B):
    x_axis = coordinates_A[0] - coordinates_B[0]
    y_axis = coordinates_A[1] - coordinates_B[1]
    # 절대값을 나중에 넣어 줘야함
    axis_sum = math.pow()
    print(math.pow(2, 3))

    return 0

result = getDistance(A, B)
print("두 점 사이의 거리는 : ", result )