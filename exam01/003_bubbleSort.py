# 버블정렬
# - 첫번째꺼랑 두번째꺼랑 비교해서 두번째꺼가 더 작으면 첫번째꺼랑 자리를 바꾼다.

numbers = [7, 3, 2, 9]

for i in range(0, len(numbers)-1): # n
    for index in range(i+1, len(numbers)): # n+1
        if numbers[i] > numbers[index]:
            # 자리를 바꿔준다.
            temp = numbers[i]
            numbers[i] = numbers[index]
            numbers[index] = temp
    print(i, '회전 :', numbers)
