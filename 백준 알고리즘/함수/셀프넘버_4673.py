
# 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.


a = 0
resultList = []
tempList = []


def solve(a):
    aList = str(a)
    for i in aList:
        a += int(i)

    return a


for i in range(1, 10001):
    a = solve(i)
    tempList.append(i)
    resultList.append(a)

for i in tempList:
    if i not in resultList:
        print(i)