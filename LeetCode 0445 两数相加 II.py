# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(l, r, i):
            if not l and not r and not i:
                return None
            s = (l.val if l else 0) + (r.val if r else 0) + i
            ans = ListNode(s % 10)
            ans.next = dfs(l.next if l else None, r.next if r else None, s // 10)
            return ans

        return self.reverseList(dfs(self.reverseList(l1), self.reverseList(l2), 0))
