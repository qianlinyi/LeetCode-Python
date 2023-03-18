from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        q = deque([(sr, sc)])
        vis = dict()
        vis[sr * n + sc] = 1
        while q:
            x, y = q.popleft()
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < m and 0 <= ny < n and image[nx][ny] == image[x][y] and (nx * n + ny not in vis):
                    vis[nx * n + ny] = 1
                    q.append((nx, ny))
            image[x][y] = color
        return image
