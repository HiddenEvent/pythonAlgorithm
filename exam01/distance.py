# 좌표평명 두 점 사이의 거리 구하는 알고리즘
# 필요 지식...
# 피타고라스의 정의
# 대각선의 제곱 = x축의 제곱 + y축의 제곱 이다라는 것, 이는 곧 아래와 같이 표현 가능
# 대각선 = 루트(x축의 제곱 + y축의 제곱)

# 좌표평면 = x축, y축
# x축은 가로
# y축은 세로
# (1,2) -> (3,4) 거리를 구해보자.
# 1)  (0,0) 에서 부터 시작해보자
import math

A = (2, 2)
B = (3, 4)

def getDistance(coordinates_A, coordinates_B):
    x_axis = coordinates_A[0] - coordinates_B[0]
    y_axis = coordinates_A[1] - coordinates_B[1]
    # x, y 2제곱(pow)의 합을 구하고,
    axis_sum = math.pow(x_axis, 2) + math.pow(y_axis, 2)

    return math.sqrt(axis_sum)

result = getDistance(A, B)
print("두 점 사이의 거리는 : ", result)