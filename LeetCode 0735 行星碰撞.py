from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for num in asteroids:
            flag = True
            while flag and num < 0 and ans and ans[-1] > 0:
                flag = ans[-1] < -num
                if ans[-1] <= -num:
                    ans.pop()
            if flag:
                ans.append(num)
        return ans
