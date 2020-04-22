import commonDef.commonInput as comInput
input_arr = comInput.sysInputArr() # input 배열

# 순차 탐색
# - 배열 A[0...n-1]에서 x를 찾는 알고리즘
def SequentialSearch(arr, n, x):
    for i in range(n):
        if arr[i] == x: return i+1
    return -1

n = len(input_arr)  # 전체 크기
x = 3   # 찾을 데이터
result = SequentialSearch(input_arr, n, x)
print(result)