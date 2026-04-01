from collections import deque


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True       

    def search(self, word: str) -> bool:
        
        # handle dot
        def dfs(node, start, word) -> bool:
            current = node
            
            for i in range(start, len(word)):
                c = word[i]
                if c == '.':
                    # check all children of current node
                    for child in current.children.values():
                        if dfs(child, i+1, word):
                            return True
                    # all children no match
                    return False
                else:
                    if c not in current.children:
                        return False
                    current = current.children[c]
            return current.is_end

        return dfs(self.root, 0, word)


