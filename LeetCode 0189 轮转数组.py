import math


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        count = math.gcd(k, n)
        print(count)
        for i in range(0, count):
            current = i
            prev = nums[i]
            for _ in range(0, n // count):
                current = (current + k) % n
                nums[current], prev = prev, nums[current]
