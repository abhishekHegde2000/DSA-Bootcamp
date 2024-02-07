'''
https://leetcode.com/problems/word-search-ii/description/

212. Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.

'''
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()  # Create an instance of Trie
        for word in words:
            trie.addWord(word)  # Use the addWord method of the Trie instance

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, path):
            if node.is_word:
                res.add(path)
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if (r, c) in visit:
                return
            if board[r][c] not in node.children:
                return

            visit.add((r, c))
            dfs(r+1, c, node.children[board[r][c]], path+board[r][c])
            dfs(r-1, c, node.children[board[r][c]], path+board[r][c])
            dfs(r, c+1, node.children[board[r][c]], path+board[r][c])
            dfs(r, c-1, node.children[board[r][c]], path+board[r][c])

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                # Use the root attribute of the Trie instance
                dfs(r, c, trie.root, "")
        return list(res)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        print(f"New TrieNode created with children: {
              self.children} and is_word: {self.is_word}")


class Trie:
    def __init__(self):
        self.root = TrieNode()
        print(f"Trie created with root: {self.root}")

    def addWord(self, word):
        node = self.root
        print(f"Adding word: {word}")
        for c in word:
            print(f"Processing character: {c}")
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        print(f"Word added, current node is_word: {node.is_word}")


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, path):
            print(f"DFS called with r: {r}, c: {
                  c}, node: {node}, path: {path}")
            if node.is_word:
                res.add(path)
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if (r, c) in visit:
                return
            if board[r][c] not in node.children:
                return

            visit.add((r, c))
            dfs(r+1, c, node.children[board[r][c]], path+board[r][c])
            dfs(r-1, c, node.children[board[r][c]], path+board[r][c])
            dfs(r, c+1, node.children[board[r][c]], path+board[r][c])
            dfs(r, c-1, node.children[board[r][c]], path+board[r][c])
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")
        return list(res)


sol = Solution()

print(sol.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], [
      # ["eat","oath"]
      "i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"]) == ["eat", "oath"])
print(sol.findWords([["a", "b"], ["c", "d"]], ["abcb"]) == [])  # []
print(sol.findWords([["a", "a"]], ["a"]) == ["a"])  # ["a"]
