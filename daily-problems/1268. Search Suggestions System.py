'''
https://leetcode.com/problems/search-suggestions-system/description

1268. Search Suggestions System
Solved
Medium
Topics
Companies
Hint
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.



Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.


Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
'''

from typing import List


class TrieNode:
    def __init__(self, char, is_end_of_word=False):
        self.char = char
        self.children = {}
        self.is_end_of_word = is_end_of_word


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(char)
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search_with_prefix(self, prefix: str) -> List[str]:
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]

        suggestions = []
        self.dfs(current_node, prefix, suggestions)
        return suggestions

    def dfs(self, node: TrieNode, current_prefix: str, suggestions: List[str]):
        if node.is_end_of_word:
            suggestions.append(current_prefix)
            if not node.children:
                return
        for child_char, child_node in node.children.items():
            self.dfs(child_node, current_prefix + child_char, suggestions)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort products lexicographically
        products.sort()
        print(f"Sorted products: {products}")

        # Build the Trie
        trie = Trie()
        for product in products:
            trie.insert(product)

        result = []
        for i in range(len(searchWord)):
            current_prefix = searchWord[:i+1]
            print(f"Current prefix: {current_prefix}")

            suggestions = trie.search_with_prefix(current_prefix)
            result.append(suggestions[:3])
            print(f"Suggestions for prefix '{
                  current_prefix}': {suggestions[:3]}")

        return result


# Example usage:
# sol = Solution()
# print(sol.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))


class TrieNode:
    def __init__(self, char, is_end_of_word=False):
        self.char = char
        self.children = {}
        self.is_end_of_word = is_end_of_word


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(char)
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search_with_prefix(self, prefix: str) -> List[str]:
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]

        suggestions = []
        self.dfs(current_node, prefix, suggestions, 0)
        return suggestions

    def dfs(self, node: TrieNode, current_prefix: str, suggestions: List[str], count: int):
        if count >= 3:
            return count
        if node.is_end_of_word:
            suggestions.append(current_prefix)
            count += 1
        for child_char, child_node in node.children.items():
            if count < 3:
                count = self.dfs(child_node, current_prefix +
                                 child_char, suggestions, count)
        return count


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort products lexicographically
        products.sort()
        print(f"Sorted products: {products}")

        # Build the Trie
        trie = Trie()
        for product in products:
            trie.insert(product)

        result = []
        for i in range(len(searchWord)):
            current_prefix = searchWord[:i+1]
            print(f"Current prefix: {current_prefix}")

            suggestions = trie.search_with_prefix(current_prefix)
            result.append(suggestions)
            print(f"Suggestions for prefix '{current_prefix}': {suggestions}")

        return result

# Example usage:
# sol = Solution()
# print(sol.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
