class Node:
    def __init__(self) -> None:
        self.child = [None] * 26
        self.isEoW = False

class Trie:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        curr = self.head
        for i in range(len(word)):
            nextPos = ord(word[i]) - ord('a')
            if not curr.child[nextPos]:
                node = Node()
                curr.child[nextPos] = node
                curr = node
            else:
                curr = curr.child[nextPos]
                

        curr.isEoW = True
            


    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            charPosition = ord(c) - ord('a')
            if not curr.child[charPosition]:
                return False
            else:
                curr = curr.child[charPosition]

        if curr.isEoW:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            charPosition = ord(c) - ord('a')
            if not curr.child[charPosition]:
                return False
            else:
                curr = curr.child[charPosition]

        return True

