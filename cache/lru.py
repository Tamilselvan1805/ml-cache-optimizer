class Node:
    def __init__(self, key):
        self.key = key
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}

        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        n = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = n
        n.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return True
        return False

    def put(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return

        node = Node(key)
        self.cache[key] = node
        self._add(node)

        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]