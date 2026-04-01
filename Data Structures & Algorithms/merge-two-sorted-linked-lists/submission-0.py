# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1
        
        node_result = node_tmp = ListNode()

        while list1 and list2: 
            if list1.val < list2.val:
                node_tmp.next = list1
                list1 = list1.next
            else:
                node_tmp.next = list2
                list2 = list2.next
            node_tmp = node_tmp.next
        
        # another list not been used in last while loop 
        node_tmp.next = list1 or list2
        # node_result.next is the node merged in first loop
        return node_result.next
