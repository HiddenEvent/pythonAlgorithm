input_arr = [8,5,1,7,6,4,3,2,9]

# 순차 탐색
# - 배열 A[0...n-1]에서 x를 찾는 알고리즘
def SequentialSearch(arr, n, x):
    for i in range(n):
        if arr[i] == x: return i+1
    return -1

n = len(input_arr)  # 전체 크기
x = 3   # 찾을 데이터
result = SequentialSearch(input_arr, n, x)
# print(result)

# 이진 탐색
# 순서대로 나열된 배열안에서 원하는 값 1개를 찾기
input_arr = [1,2,3,4,5,6,7,8,9]
def BinarySearch(arr, left, right, x):
    if left > right : return -1

    mid = (left + right)//2

    if x == arr[mid] :
        return mid
    elif x < arr[mid]: return BinarySearch(arr, left, mid-1, x)
    else : return BinarySearch(arr, mid+1, right, x)
result = BinarySearch(input_arr, 0, len(input_arr)-1, x)
print(result)