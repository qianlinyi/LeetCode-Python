class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        nums = []
        while num:
            nums.append(num % 10)
            num //= 10
        nums.reverse()
        for i in range(0, len(nums) - 1):
            mx, pos, flag = nums[i], -1, 0
            for j in range(i + 1, len(nums)):
                if nums[j] > mx:
                    flag = 1
                    mx, pos = nums[j], j
                elif nums[j] == mx:
                    pos = j
            if pos != -1 and flag:
                nums[i], nums[pos] = nums[pos], nums[i]
                break
        ans = 0
        for num in nums:
            ans = ans * 10 + num
        return ans
