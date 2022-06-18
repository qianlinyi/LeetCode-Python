# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        if not head:
            newNode.next = newNode
            return newNode
        if head.next == head:
            head.next = newNode
            newNode.next = head
            return head
        cur, nxt = head, head.next
        while nxt != head:
            if cur.val <= insertVal <= nxt.val:
                break
            if cur.val > nxt.val:
                if insertVal > cur.val or insertVal < nxt.val:
                    break
            cur = cur.next
            nxt = nxt.next
        cur.next = newNode
        newNode.next = nxt
        return head
