# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if not head.next:
        #     return None
        # first_node = head
        # length = 0
        # while head.next:
        #     length += 1
        #     head = head.next
        # length += 1
        # head = first_node

        # remove_index = length - n
        # if remove_index == 0:
        #     return head.next
        # for i in range(remove_index):
        #     if i+1 == remove_index:
        #         head.next = head.next.next
        #     else:
        #         head = head.next
        # return first_node
        return self.double_pointer(head, n)

    def double_pointer(self, head, n):
        dummy = ListNode()

        dummy.next = head

        p1 = dummy
        p2 = dummy
        for i in range(n):
            p1 = p1.next
        
        # p1 -> n
        # p2 -> 0


        while p1.next:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next

        return dummy.next