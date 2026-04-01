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
        if not head:
            return None
        copy_dict = {}
        current = head
        #copy node without next and random
        while current:
            copy_dict[current] = Node(current.val)
            current = current.next
        # update next and random with new copy node
        current = head
        while current:
            copy_dict[current].next = copy_dict.get(current.next, None)
            copy_dict[current].random = copy_dict.get(current.random, None)
            current = current.next
        return copy_dict.get(head, None)
