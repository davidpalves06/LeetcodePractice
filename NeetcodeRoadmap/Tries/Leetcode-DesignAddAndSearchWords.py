class Node:
    def __init__(self) -> None:
        self.child = [None] * 26
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        curr = self.head
        for c in word:
            nextPos = ord(c) - ord('a')
            if not curr.child[nextPos]:
                node = Node()
                curr.child[nextPos] = node
                curr = node
            else:
                curr = curr.child[nextPos]

        curr.isWord = True


    def search(self, word: str) -> bool:
        def dfs(position,node):
            curr = node
            for i in range(position,len(word)):
                char = word[i]
                if char == '.':
                    for child in curr.child:
                        if child and dfs(i+1,child):
                            return True
                    return False
                else:
                    nextPosition = ord(char) - ord('a')
                    if not curr.child[nextPosition]:
                        return False
                    else:
                        curr = curr.child[nextPosition]
            
            return curr.isWord
            
        return dfs(0,self.head)


