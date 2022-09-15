# 降低搜索空间
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        seen = set()
        for i in range(2 ** 4):
            pressArr = [(i >> j) & 1 for j in range(4)]  # 四个按钮的按动情况
            if sum(pressArr) % 2 == presses % 2 and sum(pressArr) <= presses:  # 按压次数和按动情况一致
                status = pressArr[0] ^ pressArr[2] ^ pressArr[3]
                if n >= 2:
                    status |= (pressArr[0] ^ pressArr[1]) << 1
                if n >= 3:
                    status |= (pressArr[0] ^ pressArr[2]) << 2
                if n >= 4:
                    status |= (pressArr[0] ^ pressArr[1] ^ pressArr[3]) << 3
                seen.add(status)
        return len(seen)
