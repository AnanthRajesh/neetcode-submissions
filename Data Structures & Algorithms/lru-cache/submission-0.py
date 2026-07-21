class Node:
    """
    Node for the doubly linked list.
    Each node stores:
        key   -> needed so we can remove it from the hashmap during eviction
        val   -> value associated with the key
        prev  -> previous node
        next  -> next node
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity

        # Dictionary maps key -> corresponding node
        self.cache = {}

        # Dummy nodes
        # left  = Least Recently Used (LRU)
        # right = Most Recently Used (MRU)
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Connect the dummy nodes
        self.left.next = self.right
        self.right.prev = self.left

    # ---------------------------------------------------
    # Remove a node from the doubly linked list
    # ---------------------------------------------------
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # ---------------------------------------------------
    # Insert a node right before the MRU dummy node
    # This makes it the most recently used item.
    # ---------------------------------------------------
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    # ---------------------------------------------------
    # Return value if key exists.
    # Since it was accessed, move it to MRU.
    # ---------------------------------------------------
    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move node to MRU position
        self.remove(node)
        self.insert(node)

        return node.val

    # ---------------------------------------------------
    # Insert or update a key
    # ---------------------------------------------------
    def put(self, key: int, value: int) -> None:

        # If key already exists, remove old node
        if key in self.cache:
            self.remove(self.cache[key])

        # Create a fresh node
        node = Node(key, value)

        # Store in hashmap
        self.cache[key] = node

        # Move to MRU position
        self.insert(node)

        # If capacity exceeded, remove LRU node
        if len(self.cache) > self.cap:

            # First real node after left dummy
            lru = self.left.next

            # Remove from linked list
            self.remove(lru)

            # Remove from hashmap
            del self.cache[lru.key]