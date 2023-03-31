class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(grid), len(grid[0])
        for i in range(n):
            x, y = 0, i
            flag = True
            while 0 <= x < m and 0 <= y < n:
                print(x, y)
                if grid[x][y] == 1:
                    if y == n - 1 or grid[x][y + 1] == -1:
                        flag = False
                        ans.append(-1)
                        break
                    else:
                        x, y = x + 1, y + 1
                else:
                    if y == 0 or grid[x][y - 1] == 1:
                        flag = False
                        ans.append(-1)
                        break
                    else:
                        x, y = x + 1, y - 1
            if flag:
                ans.append(y)
        return ans
