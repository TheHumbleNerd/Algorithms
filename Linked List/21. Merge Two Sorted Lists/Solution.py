# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        last = None
        h1, h2 = list1, list2
        if (h1 and h2 and h1.val < h2.val) or (h1 and not h2):
            newHead = list1
            h1 = list1.next
            h2 = list2
        elif list2 is not None:
            newHead = list2
            h1 = list2.next
            h2 = list1

        last = newHead
        while h1 and h2:
            if h1.val < h2.val:
                last.next = h1
                h1 = h1.next
            else:
                last.next = h2
                h2 = h2.next
            last = last.next
        
        if h1:
            last.next = h1
        elif h2:
            last.next = h2

        return newHead
