from collections import deque

class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class LinkedList:
    
    def __init__(self):
        self._list = deque()
        self.head = None
    def get(self, index: int) -> int:
        if index >= len(self._list):
            return -1
        return self._list[index].val

    def insertHead(self, val: int) -> None:
        node = Node(val, None)
        if not self.head:
            self._list.append(node)
        else:
            self._list.appendleft(node)
            node.next = self.head
        self.head = node

    def insertTail(self, val: int) -> None:
        node = Node(val, 0)
        if self._list:
            last_node = self._list[-1]
            last_node.next = node
        else:
            self.head = node
        self._list.append(node)

    def remove(self, index: int) -> bool:
        if index >= len(self._list):
            return False
        if index == 0:
            self.head = self.head.next
        else:
            prev_node = self._list[index-1]
            delete_node = self._list[index] 
            prev_node.next = delete_node.next
        del self._list[index]
        return True


    def getValues(self) -> List[int]:
        return [node.val for node in self._list]        
