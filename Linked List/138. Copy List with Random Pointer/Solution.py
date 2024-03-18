"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {None : None}
        iter = head
        while iter:
            n = Node(iter.val)
            map[iter] = n
            iter = iter.next
        
        iter = head
        while iter:
            map[iter].next = map[iter.next]
            map[iter].random = map[iter.random]
            iter = iter.next
        
        return map[head]
