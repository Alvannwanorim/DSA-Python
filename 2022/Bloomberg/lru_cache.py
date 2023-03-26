class DLinkedListNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self_lru_cache = self._head_node = DLinkedListNode()
        self._tail_node = DLinkedListNode()

        self._head_node.next = self._tail_node
        self._tail_node = self._head_node

        self.existing_nodes = {}
    def _add_to_head(self, node: DLinkedListNode):
        self._head_node.next, node.next = node, self._head_node.next
        node.prev, node.next.prev = self._head_node, node

        self.existing_nodes[node.key] = node
        
        if len(self.existing_nodes) > self.capacity:
            self._remove_node_from_tail()
    def _remove_node_from_tail(self):
        node = self._tail_node.prev
        self._remove_node(node)
        del self.existing_nodes[node.key]
        return

    def _remove_node(self, node: DLinkedListNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        return


    def get(self, key: int) -> int:
        if key not in self.existing_nodes:
            return -1 
        else:
            node = self.existing_nodes[key]
            self._remove_node(node)
            self._add_to_head(node)
            return node.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.existing_nodes[key]:
            node = DLinkedListNode(key, value)
        else:
            node = self.existing_nodes[key]
            node.val = value
            self._remove_node(node)
        
        self._add_to_head(node)
        return 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)