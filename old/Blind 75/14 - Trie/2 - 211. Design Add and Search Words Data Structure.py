'''
https://leetcode.com/problems/design-add-and-search-words-data-structure/

211. Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.

'''

# class WordDictionary:

#     def __init__(self):


#     def addWord(self, word: str) -> None:


#     def search(self, word: str) -> bool:


# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)


class TrieNode:
    def __init__(self):
        # Initialize a TrieNode with an empty dictionary of children and a word flag set to False
        self.children = {}
        self.is_word = False
        print(f"New TrieNode created with children: {
              self.children} and is_word: {self.is_word}")


class WordDictionary:
    def __init__(self):
        # Initialize a WordDictionary with a root TrieNode
        self.root = TrieNode()
        print(f"WordDictionary created with root: {self.root}")

    def addWord(self, word: str) -> None:
        # Start from the root node
        current_node = self.root
        print(f"Adding word: {word}")
        for character in word:
            print(f"Processing character: {character}")
            # If the character is not in the current node's children, add a new TrieNode
            if character not in current_node.children:
                current_node.children[character] = TrieNode()
            # Move to the child node
            current_node = current_node.children[character]
        # After all characters are processed, mark the current node as a word
        current_node.is_word = True
        print(f"Word added, current node is_word: {current_node.is_word}")

    def search(self, word: str) -> bool:
        print(f"Searching for word: {word}")

        def dfs(index, node):
            current_node = node
            print(f"DFS called with index: {index} and node: {current_node}")
            for i in range(index, len(word)):
                character = word[i]
                print(f"Processing character: {character}")
                # If the character is a '.', iterate over all child nodes and recursively call dfs on them
                if character == '.':
                    for child_node in current_node.children.values():
                        if dfs(i + 1, child_node):
                            return True
                    return False
                else:
                    # If the character is not in the current node's children, return False
                    if character not in current_node.children:
                        return False
                    # Move to the child node
                    current_node = current_node.children[character]
            # After all characters are processed, return whether the current node is a word
            return current_node.is_word

        # Call dfs on the root node and return its result
        return dfs(0, self.root)


class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()  # create an empty root with no children
        print(f"New WordDictionary created. Root: {self.root}")

    def addWord(self, word: str) -> None:
        currentNode = self.root
        print(f"Adding word: {word}")

        for char in word:
            print(f"Processing character: {char}")
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
                print(f"New node created for character: {char}")
            currentNode = currentNode.children[char]

        currentNode.end = True
        print(f"Word added. End of Word marked at node: {currentNode}")

    def search(self, word: str) -> bool:

        def dfs(node, i):
            print(f"DFS at index: {i}, node: {node}")

            if i == len(word):
                return node.end

            if word[i] == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
            else:
                if word[i] in node.children:
                    return dfs(node.children[word[i]], i + 1)

            return False

        return dfs(self.root, 0)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Example usage:
word_dict = WordDictionary()
word_dict.addWord("bad")
word_dict.addWord("dad")
word_dict.addWord("mad")

print(word_dict.search("pad"))  # Output: False
print(word_dict.search("bad"))  # Output: True
print(word_dict.search(".ad"))  # Output: True
print(word_dict.search("b.."))  # Output: True
