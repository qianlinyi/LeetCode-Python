from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0 for _ in range(2 * n)]
        for i, num in enumerate(nums[:n]):
            ans[i << 1] = num
            ans[i << 1 | 1] = nums[i + n]
        return ans
