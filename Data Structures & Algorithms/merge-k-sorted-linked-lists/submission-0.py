import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        dummy = ListNode()
        heap = []
        p = dummy
        count = 0
        for node in lists:
            if node is not None:
                heapq.heappush(heap, (node.val, count, node))
                count += 1

        while heap:
            val, _, node = heapq.heappop(heap)
            p.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1

            p = p.next

        return dummy.next



