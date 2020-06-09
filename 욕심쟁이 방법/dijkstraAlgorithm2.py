import numpy as np
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


from collections import defaultdict
import heapq

# 우선순위 큐를 이용한 다익스트라 알고리즘 접근
def dijkstra_heapq(graph, initial, target): # 그래프 정보, 시작,도착점을 인자값으로 넘긴다.
    visited = {initial: 0} # 시작점 a에 0을 세팅
    h = [(0, initial)]
    path = {}
    nodes = set(graph.nodes)
    while nodes and h:
        current_weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                current_weight, min_node = heapq.heappop(h)
        except IndexError:
            break

        if min_node == target:
            return visited, path

        nodes.remove(min_node)

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, v]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heapq.heappush(h, (weight, v))
                path[v] = min_node

    return visited, path

if __name__ == "__main__":
    gr = Graph()
    gr.add_node("a")
    gr.add_node("b")
    gr.add_node("c")
    gr.add_node("d")
    gr.add_node("e")
    gr.add_node("f")
    gr.add_node("g")
    gr.add_node("z")
    gr.add_edge("a", "b", 4)
    gr.add_edge("a", "c", 3)
    gr.add_edge("b", "c", 2)
    gr.add_edge("b", "d", 5)
    gr.add_edge("c", "d", 3)
    gr.add_edge("c", "e", 6)
    gr.add_edge("d", "e", 1)
    gr.add_edge("d", "f", 5)
    gr.add_edge("e", "g", 5)
    gr.add_edge("f", "g", 2)
    gr.add_edge("f", "z", 7)
    gr.add_edge("g", "z", 4)
    visited, path = dijkstra_heapq(gr, "a", "z")
    print("각 꼭지점의 최단경로 : ",visited)
    start = "a"
    end = "z"
    result = []
    while end != start:
        result.append(end)
        end = path[end]
    result.append(end)

    print("최단 경로 : ", end=' ')
    lastLeng = len(result)
    for i in range(0,lastLeng):
        if i == lastLeng-1 :
            print(result.pop())
        else :
            print(result.pop(), end=' -> ')