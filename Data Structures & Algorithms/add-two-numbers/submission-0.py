# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = []
        head = current = ListNode(0, None)
        def add_node(l1, l2, current, prev, tmp_value):
            if not l1 and not l2 and not tmp_value:
                return
            if not current:
                current = ListNode(0, None)
                prev.next = current
            a, b = 0, 0
            if l1:
                a = l1.val
            if l2:
                b = l2.val
            c = (a+b+tmp_value) % 10
            tmp_value = (a+b+tmp_value) // 10
            current.val = c
            add_node(l1.next if l1 else None, l2.next if l2 else None, current.next, current, tmp_value)
        add_node(l1,l2, current, current, 0)
        return head
        