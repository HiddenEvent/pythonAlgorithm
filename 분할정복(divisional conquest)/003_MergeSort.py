# 합병정렬
input_arr = [20, 15, 35, 50, 40, 10, 30, 25]

def MergeSort(arr, n):
    if n > 1 : # 1이 될때 까지 분할 해줌
        Mid = n//2
        A = MergeSort(arr[0:Mid], Mid) # 왼쪽 분할
        B = MergeSort(arr[Mid:n], n-Mid) # 오른쪽 분할
        arr = Merge(A, B, Mid, n-Mid) # 합병을 위한 함수 호출
    
    return arr
def Merge(A, B, n, m):
    sort_arr = []
    i = j = k = 0

    return sort_arr


result = MergeSort(input_arr, len(input_arr))
