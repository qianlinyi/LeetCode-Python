import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        cnt = 0
        for num in nums:
            if num:
                p *= num
            else:
                cnt += 1
        ans = []
        for num in nums:
            if cnt > 1:
                ans.append(0)
            else:
                if cnt == 1:
                    if num == 0:
                        ans.append(p)
                    else:
                        ans.append(0)
                else:
                    ans.append(p // num)
        return ans
