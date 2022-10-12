# Definition for singly-linked list.
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        ans, exist = 0, defaultdict(int)
        for num in nums:
            exist[num] = 1
        while head:
            flag = 0
            while head and head.val in exist:
                flag = 1
                head = head.next
            if flag:
                ans += 1
            if head:
                head = head.next
        return ans
