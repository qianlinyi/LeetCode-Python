from typing import List
import heapq


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = [[] for _ in range(n)]  # 邻接表
        for u, v, c in edges:
            self.graph[u].append((v, c))

    def addEdge(self, edge: List[int]) -> None:
        u, v, c = edge
        self.graph[u].append((v, c))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [-1] * self.n  # 最短距离数组，初始为-1
        dist[node1] = 0
        visited = [False] * self.n  # 记录节点是否被访问过
        pq = [(0, node1)]  # 小根堆，记录最短距离和节点编号
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
