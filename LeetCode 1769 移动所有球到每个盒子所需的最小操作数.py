from bisect import bisect_right


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        pos = []
        ans = [0] * len(boxes)
        for idx, box in enumerate(boxes):
            if box == '1':
                pos.append(idx)
        if len(pos) == 0:
            return ans
        sum = [0] * len(pos)
        for i, v in enumerate(pos):
            if i == 0:
                sum[i] = pos[i]
            else:
                sum[i] = sum[i - 1] + pos[i]

        for i in range(len(boxes)):
            p = bisect_right(pos, i)
            ans[i] = sum[-1] - (0 if p == 0 else sum[p - 1]) - i * (len(pos) - p) + (i * p - sum[p - 1] if p else 0)
        return ans
