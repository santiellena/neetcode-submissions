class PrefixTree:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = PrefixTree()

            curr = curr.children[ch]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
        
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for ch in prefix:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
        
        return True
        