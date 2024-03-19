class Node:
    def __init__(self, key:int, val: int):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def removeNode(self, node: Node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def insertNodeAtRight(self, node:Node):
        lastNode = self.right.prev
        lastNode.next = node
        node.prev = lastNode
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.removeNode(self.cache[key])
            self.insertNodeAtRight(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
            self.cache[key].val = value
        else:
            self.cache[key] = Node(key, value)
        self.insertNodeAtRight(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lruNode = self.left.next
            self.removeNode(lruNode)
            del self.cache[lruNode.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
