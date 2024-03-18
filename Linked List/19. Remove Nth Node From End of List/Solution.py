# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        current, last = head, head
        for i in range(n):
            last = last.next
        
        while last:
            prev = current
            current = current.next
            last = last.next
        
        newHead = None
        if prev:
            prev.next = current.next
            newHead = head
        else:
            newHead = head.next

        return newHead
