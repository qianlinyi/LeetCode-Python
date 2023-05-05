import heapq
from collections import defaultdict


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = edges

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [-1] * self.n  # 最短距离数组，初始为-1
        dist[node1] = 0
        visited = [False] * self.n  # 记录节点是否被访问过
        pq = [(node1, 0)]  # 小根堆，记录最短距离和节点编号
        while pq:
            cur_dist, cur_node = heapq.heappop(pq)
            if visited[cur_node]:  # 跳过已经访问过的节点
                continue
            visited[cur_node] = True
            if cur_node == node2:  # 找到终点，直接返回
                return dist[node2]
            for next_node, next_dist in self.graph[cur_node]:
                if visited[next_node]:  # 跳过已经访问过的节点
                    continue
                if dist[next_node] == -1 or cur_dist + next_dist < dist[next_node]:
                    dist[next_node] = cur_dist + next_dist
                    heapq.heappush(pq, (dist[next_node], next_node))
        return -1  # 没有找到路径


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        id = 0
        mp1 = dict()  # id to point
        mp2 = dict()  # point to id
        cost = defaultdict(int)
        mp1[id] = (start[0], start[1])
        mp2[(start[0], start[1])] = id
        id += 1
        mp1[id] = (target[0], target[1])
        mp2[(target[0], target[1])] = id
        id += 1
        for road in specialRoads:
            if (road[0], road[1]) not in mp2:
                mp1[id] = (road[0], road[1])
                mp2[(road[0], road[1])] = id
                id += 1
            if (road[2], road[3]) not in mp2:
                mp1[id] = (road[2], road[3])
                mp2[(road[2], road[3])] = id
                id += 1
            x = mp2[(road[0], road[1])]
            y = mp2[(road[2], road[3])]
            if (x, y) not in cost:
                cost[(x, y)] = road[4]
            else:
                cost[(x, y)] = min(cost[(x, y)], road[4])
        # build graph
        edges = [[] for _ in range(id)]
        for i in range(id):
            for j in range(id):
                edges[i].append((j, min(cost[(i, j)] if (i, j) in cost else 2 * 10 ** 5,
                                        abs(mp1[i][0] - mp1[j][0]) + abs(mp1[i][1] - mp1[j][1]))))
        g = Graph(id, edges)
        return g.shortestPath(0, 1)
