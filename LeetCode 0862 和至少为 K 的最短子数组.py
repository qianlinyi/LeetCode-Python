class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        preSumArr = [0]
        res = len(nums) + 1
        for num in nums:
            preSumArr.append(preSumArr[-1] + num)
        q = deque()
        for i, curSum in enumerate(preSumArr):
            while q and curSum - preSumArr[q[0]] >= k:
                res = min(res, i - q.popleft())
            while q and preSumArr[q[-1]] >= curSum:
                q.pop()
            q.append(i)
        return res if res < len(nums) + 1 else -1
