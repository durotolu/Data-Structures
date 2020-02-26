from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = DoublyLinkedList()
        self.dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.dict:
            return None
        
        node = self.dict[key]

        # small optimization
        if self.storage.tail == node:
            return node.value

        self.storage.move_to_end(node)
        return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.dict:
            #node = ListNode(self.dict[key], value)
            # print(node, 186)
            node = self.dict[key]
            node.value = (key, value)

            if self.storage.tail != node:
                self.storage.move_to_end(node)
            return
        else:
            #new_node = ListNode(key, value)
            if self.storage.length == self.limit:
                del self.dict[self.storage.head.value[0]]
                self.storage.remove_from_head()
                self.size -= 1
            self.storage.add_to_tail((key, value))
            self.dict[key] = self.storage.tail
            self.size += 1


cache = LRUCache(3)
cache.set('item1', 'a')
cache.set('item2', 'b')
cache.set('item3', 'c')
b = cache.get('item1')
cache.set('item4', 'd')

print(cache.get('item1'))
print(cache.get('item3'))
print(cache.get('item4'))
print(cache.get('item2'))