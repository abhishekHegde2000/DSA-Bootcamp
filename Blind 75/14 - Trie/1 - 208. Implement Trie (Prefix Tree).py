'''
https://leetcode.com/problems/implement-trie-prefix-tree/

208. Implement Trie (Prefix Tree)

208. Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

'''

# class Trie:

#     def __init__(self):


#     def insert(self, word: str) -> None:


#     def search(self, word: str) -> bool:


#     def startsWith(self, prefix: str) -> bool:


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False
        print(f"New TrieNode created. Children: {
              self.children}, End of Word: {self.endOfWord}")


class Trie:

    def __init__(self):
        self.root = TrieNode()
        print(f"New Trie created. Root: {self.root}")

    def insert(self, word: str) -> None:
        currentNode = self.root
        print(f"Inserting word: {word}")

        for char in word:
            print(f"Processing character: {char}")
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
                print(f"New node created for character: {char}")
            currentNode = currentNode.children[char]

        currentNode.endOfWord = True
        print(f"Word inserted. End of Word marked at node: {currentNode}")

    def search(self, word: str) -> bool:
        currentNode = self.root
        print(f"Searching for word: {word}")

        for char in word:
            print(f"Processing character: {char}")
            if char not in currentNode.children:
                print(f"Character not found. Word does not exist.")
                return False
            currentNode = currentNode.children[char]

        print(f"Word found. End of Word: {currentNode.endOfWord}")
        return currentNode.endOfWord

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        print(f"Checking if any word starts with prefix: {prefix}")

        for char in prefix:
            print(f"Processing character: {char}")
            if char not in currentNode.children:
                print(f"Character not found. No word starts with prefix.")
                return False
            currentNode = currentNode.children[char]

        print(f"Prefix found.")
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))
