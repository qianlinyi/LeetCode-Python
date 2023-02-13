class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        cx = cy = 0
        res = []
        for c in target:
            c = ord(c) - ord('a')
            nx = c // 5
            ny = c % 5
            if nx < cx:
                res.append('U' * (cx - nx))
            if ny < cy:
                res.append('L' * (cy - ny))
            if nx > cx:
                res.append('D' * (nx - cx))
            if ny > cy:
                res.append('R' * (ny - cy))
            res.append('!')
            cx, cy = nx, ny
        return ''.join(res)
