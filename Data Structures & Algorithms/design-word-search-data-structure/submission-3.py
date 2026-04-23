class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        The same approach as in the implementataton of Prefix Tree Data Structure and its operations. 
        """
        curr = self.root 
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
        

    def search(self, word: str) -> bool:
        """
        bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
        word may contain dots '.' where dots can be matched with any letter.
        """

        # Define Recursive function
        def dfs(j, root):
            # pointer cur starts at node that was passed-in
            cur = root

            # Start looping over character from passed in index in the word
            for i in range(j, len(word)):
                # Get the character at the index
                c = word[i]
                # Character can be a-z (easy case) and . (hard case)
                
                # . case 
                if c == ".":
                    # if char is ., we loop over all over its children and call recursive function on them, doing DFS and going deeper
                    for child in cur.children.values():
                        if dfs(i + 1, child): # if DFS hits True, we return true 
                            return True
                    return False
                
                # a-z case 
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end

        # Call recursive function 
        return dfs(0, self.root)
        
