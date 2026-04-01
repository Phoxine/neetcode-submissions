# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        

        i, j = 0, len(node_list) - 1
        while i < j:
            node_list[i].next = node_list[j]
            i += 1
            if i >= j:
                break
            node_list[j].next = node_list[i]
            j -= 1

        node_list[i].next = None