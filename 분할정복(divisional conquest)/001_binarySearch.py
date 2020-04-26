# 이진 탐색( 정렬된 데이터인 경우 사용)
# 순서대로 나열된 배열안에서 원하는 값 1개를 찾기
input_arr = [1,2,3,4,5,6,7,8,9]
x = 3   # 찾을 데이터

def BinarySearch(arr, left, right, x):
    if left > right : return -1

    mid = (left + right)//2

    if x == arr[mid] :
        return mid
    elif x < arr[mid]: return BinarySearch(arr, left, mid-1, x)
    else : return BinarySearch(arr, mid+1, right, x)
result = BinarySearch(input_arr, 0, len(input_arr)-1, x)
print(result)