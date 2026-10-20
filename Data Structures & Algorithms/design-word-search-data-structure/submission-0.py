class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)        

    
    def _dfs(self, word: str, start_idx: int, node: TrieNode) -> bool:
        curr = node

        for i in range(start_idx, len(word)):
            c = word[i]

            if c == ".":
                for child in curr.children.values():
                    if self._dfs(word, i + 1, child):
                        return True
                return False

            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
        
        return curr.word
