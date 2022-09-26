from typing import List


# 排序
# class Solution:
#     def missingTwo(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         n, index, miss = 1, 0, []
#         while index < len(nums):
#             if nums[index] == n:
#                 index += 1
#                 n += 1
#             else:
#                 miss.append(n)
#                 n += 1
#         while len(miss) < 2:
#             miss.append(n)
#             n += 1
#         return miss

# 位运算
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        xorsum = 0
        n = len(nums) + 2
        for num in nums:
            xorsum ^= num
        for i in range(1, n + 1):
            xorsum ^= i

        lsb = xorsum & (-xorsum)
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num
        for i in range(1, n + 1):
            if i & lsb:
                type1 ^= i
            else:
                type2 ^= i
        return [type1, type2]
