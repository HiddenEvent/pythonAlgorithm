## 재귀(recursive)
# - 재귀는 자기 자신을 호출하는 것을 말한다
## 재귀함수(recursive function)
# - 자기 자신을 호출하는 함수를 말한다.

arr = [7, 3, 2, 9]


def sum(arr, accu=0):
    if len(arr) == 0:
        return accu
    return sum(arr, accu + arr.pop())


result = sum(arr)
print(result)
