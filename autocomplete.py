# trie implementation with a count of min autcomplete for all words
class Node:
    def __init__(self, value):
        self.freq = 0
        self.value = value
        self.children = {}
    def insert(self, s, idx):
        self.freq += 1
        if idx != len(s):
            self.children.setdefault(s[idx], Node(s[idx]))
            self.children.get(s[idx]).insert(s, idx + 1)
    
    def query(self, s, idx):
        if self.freq == 1 or len(s) == idx:
            return 0
        return self.children.get(s[idx]).query(s, idx + 1) + 1
        

def autocomplete(words: List[str]) -> int:
    trie = Node('$')
    total = 0
    for word in words:
        trie.insert(word, 0)
        total += trie.query(word, 0)
    return total + 1
