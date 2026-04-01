class Node:
    def __init__(self):
        self.is_end = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        node = self.head
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.head
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c] 
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        