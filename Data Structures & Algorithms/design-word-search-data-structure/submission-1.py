class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word: str) -> None:
        curr = self

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = WordDictionary()
        
            curr = curr.children[ch]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self

        for i in range(len(word)):
            if word[i] == ".":
                found = False
                keys = curr.children.keys()
                copy_word = word
                
                for key in keys:
                    copy_word = copy_word[:i] + key + copy_word[i + 1:]
                    found = found or self.search(copy_word)

                return found
            elif word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        
        return curr.isWord
