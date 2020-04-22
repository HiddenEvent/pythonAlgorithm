# 퀵정렬
# 8,5,1,7,6,4,3,2,9 데이터를 퀵정렬하기

numbers = [8,5,1,7,6,4,3,2,9]

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [number for number in array[1:] if number < pivot]
        greater = [number for number in array[1:] if number > pivot]
        print(less)
        return quickSort(less) + [pivot] + quickSort(greater) # 재귀 호출
result = quickSort(numbers)
# print(result)