from collections import Counter


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = -1
        cnt = [0] * (max(nums) + k * 2)

        def dfs(i: int) -> None:
            if i == len(nums):
                nonlocal ans
                ans += 1
                return
            dfs(i + 1)
            x = nums[i]
            if cnt[x - k] == 0 and cnt[x + k] == 0:
                cnt[x] += 1
                dfs(i + 1)
                cnt[x] -= 1

        dfs(0)
        return ans
