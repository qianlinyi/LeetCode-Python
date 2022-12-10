class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        mx, end, step = 0, 0, 0
        for i in range(n - 1):
            if mx >= i:
                mx = max(mx, i + nums[i])
                if i == end:
                    end = mx
                    step += 1
        return step
