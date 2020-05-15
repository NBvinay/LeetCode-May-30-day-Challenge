# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.root = {}
        self.startSymbol = "*"
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word :
            if not char in node :
                node[char] = {}
            node = node[char]
        node[self.startSymbol] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        # print (node)
        for char in word :
            if not char  in node :
                return False
            node = node[char]
        return self.startSymbol in node
        
            

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        node = self.root
        for char in prefix :
            if not char in node :
                return False
            node = node[char]
        return True
    
    