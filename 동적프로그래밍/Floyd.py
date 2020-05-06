#플로이드 알고리즘

# 첫째 줄에 도시의 개수 n(1 ≤ n ≤ 100)이 주어지고
# 둘째 줄에는 버스의 개수 m(1 ≤ m ≤ 100,000)이 주어진다.
# 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다.
# 처음에는 그 버스의 출발 도시의 번호가 주어진다
# 버스의 시작 도시 a
# 도착 도시 b
# 한 번 타는데 필요한 비용 c

# 입력 예제
# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4

# 출력 예제
# 0 2 3 1 4
# 12 0 15 2 5
# 8 5 0 1 1
# 10 7 13 0 3
# 7 4 10 6 0

n = int(input())
m = int(input())
bus_cost = [[100001 for _ in range(n+1)] for _ in range(n+1)] # 인접행렬로 초기화
print(bus_cost)
for _ in range(m):
    start, end, cost = map(int, input().split())
    bus_cost[start][end] = min(cost, bus_cost[start][end])

#플로이드-워셜 알고리즘
for k in range(1, n+1): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: #자기 자신으로 오는 경우는 없다고 했으므로
                bus_cost[i][j] = 0
            else: #경로 거치는 것 or 직접 가는 것 or 이전 경로들
                bus_cost[i][j] = min(bus_cost[i][j],
                                     bus_cost[i][k] + bus_cost[k][j])


#출력
for row in bus_cost[1:]:
    for col in row[1:]:
        if col == 100001:
            print(0, end = " ")
        else:
            print(col, end = " ")
    print()