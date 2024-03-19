# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummyNode = ListNode()
        last = dummyNode
        while l1 and l2:
            if l1.val < l2.val:
                last.next = l1
                l1 = l1.next
            else:
                last.next = l2
                l2 = l2.next
            last = last.next
        
        if l1:
            last.next = l1
        elif l2:
            last.next = l2
        
        return dummyNode.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)

        if l == 0:
            return None
        elif l == 1:
            return lists[0]

        half = l//2
        res1 = self.mergeKLists(lists[0:half])
        res2 = self.mergeKLists(lists[half:l])
        return self.mergeTwoLists(res1, res2)
