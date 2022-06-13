from typing import List


# 基本排序
# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         ans, new_heights = 0, sorted(heights)
#         for i in range(len(heights)):
#             ans += heights[i] != new_heights[i]
#         return ans

# 桶排
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt, index, ans = [0] * (max(heights) + 1), 0, 0
        for height in heights:
            cnt[height] += 1
        for i in range(1, max(heights) + 1):
            for j in range(cnt[i]):
                if heights[index] != i:
                    ans += 1
                index += 1
        return ans
