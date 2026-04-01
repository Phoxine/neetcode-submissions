# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tmp_node = []
        if not head:
            return False
        while head not in tmp_node :
            tmp_node.append(head)
            head = head.next
            if not head:
                return False
        return True
        