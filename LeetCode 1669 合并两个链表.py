# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode()
        head, tail = ListNode(), ListNode()
        dummy.next = list1
        prev = dummy
        idx = 0
        while prev:
            if idx == a:
                head = prev
            if idx == b + 1:
                tail = prev.next
            idx += 1
            prev = prev.next
        head.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = tail
        return list1
