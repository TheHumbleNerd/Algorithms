# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle of the list
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        #reverse second half
        prev = None
        current = s.next
        s.next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        #merge first and second half
        h1, h2 = head, prev
        while h1 and h2:
            next1 = h1.next
            h1.next = h2
            next2 = h2.next
            h2.next = next1
            h1 = next1
            h2 = next2
