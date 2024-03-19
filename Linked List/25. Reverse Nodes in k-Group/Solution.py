# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKth(self, s: Optional[ListNode], k: int) -> Optional[ListNode]:
        for i in range(k-1):
            if s:
                s = s.next
            else:
                break
        return s

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newHead = head
        groupPrev = None
        groupStart = head
        while True:
            groupLast = self.getKth(groupStart, k)
            if groupLast is None:
                break

            groupNext = groupLast.next

            current = groupStart
            prev = groupNext
            while current != groupNext:
                next = current.next
                current.next = prev
                prev = current
                current = next
            
            if not groupPrev:
                newHead = prev
            else:
                groupPrev.next = groupLast

            groupPrev = groupStart
            groupStart = current

        return newHead
