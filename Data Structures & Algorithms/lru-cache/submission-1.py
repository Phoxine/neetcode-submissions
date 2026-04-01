class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left_node = Node()
        self.right_node = Node()
        self.left_node.next = self.right_node
        self.right_node.prev = self.left_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # marked as currently used
            next_node, prev_node = node.next, node.prev
            prev_node.next, next_node.prev = next_node, prev_node
            last_node, right_node = self.right_node.prev, self.right_node
            last_node.next = right_node.prev =  node
            node.prev, node.next = last_node, right_node
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            tmp_node = self.cache[key]
            tmp_node.val = value
            node_a, node_b = tmp_node.prev, tmp_node.next
            node_a.next, node_b.prev = node_b, node_a
            last_node = self.right_node.prev
            last_node.next = tmp_node
            self.right_node.prev = tmp_node
            tmp_node.next, tmp_node.prev = self.right_node, last_node
            return

        new_node = Node(key=key, val=value)
        self.cache[key] = new_node
        if len(self.cache) > self.capacity:
            removed_node = self.left_node.next
            removed_node_next = removed_node.next
            self.left_node.next, removed_node_next.prev = removed_node_next, self.left_node
            del self.cache[removed_node.key]
            last_node = self.right_node.prev
            last_node.next = new_node
            self.right_node.prev = new_node
            new_node.next, new_node.prev = self.right_node, last_node
        else:
            prev_node = self.right_node.prev
            prev_node.next = self.right_node.prev = new_node
            new_node.next, new_node.prev = self.right_node, prev_node


        

