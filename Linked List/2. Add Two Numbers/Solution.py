# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result, h = None, None
        carry = 0
        h1, h2 = l1, l2
        while h1 and h2:
            s = h1.val+h2.val+carry
            carry = s//10
            r = s%10
            n = ListNode(r)
            if h:
                h.next = n
                h = h.next
            else:
                result = n
                h = result
            h1 = h1.next
            h2 = h2.next
        
        l = None
        if h1:
            l = h1
        elif h2:
            l = h2
        
        while l:
            s = l.val+carry
            carry = s//10
            r = s%10
            n = ListNode(r)
            h.next = n
            h = h.next
            l = l.next
        
        if carry is not 0:
            n = ListNode(carry)
            h.next = n

        return result
