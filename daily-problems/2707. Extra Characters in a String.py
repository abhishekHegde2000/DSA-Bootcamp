'''
https://leetcode.com/problems/extra-characters-in-a-string/description/

2707. Extra Characters in a String

You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

 

Example 1:

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:

Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
 

Constraints:

1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words

'''

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Memoization dictionary to store the minimum extra characters for each index
        memo = {}

        def dfs(index):
            # Print the current index being processed
            print(f"Processing index: {index}")

            # Base case: if index reaches the end of the string, no extra characters are needed
            if index == len(s):
                print(f"Reached end of string at index: {index}")
                return 0

            # If the result for this index is already computed, return it
            if index in memo:
                print(f"Memo hit for index {index}: {memo[index]}")
                return memo[index]

            # Initialize the minimum extra characters to a large number
            min_extra_chars = float('inf')
            print(f"Initial min_extra_chars: {min_extra_chars}")

            # Try to match each word in the dictionary with the substring starting at the current index
            for word in dictionary:
                if s[index:index+len(word)] == word:
                    print(f"Word '{word}' matches at index {index}")
                    min_extra_chars = min(
                        min_extra_chars, dfs(index + len(word)))
                    print(f"Updated min_extra_chars after matching word '{
                          word}': {min_extra_chars}")

            # Consider the case where the current character is an extra character
            min_extra_chars = min(min_extra_chars, 1 + dfs(index + 1))
            print(f"Updated min_extra_chars after considering extra character at index {
                  index}: {min_extra_chars}")

            # Store the result in memoization dictionary
            memo[index] = min_extra_chars
            print(f"Memoizing: index {
                  index}, min_extra_chars {min_extra_chars}")

            return min_extra_chars

        # Start the depth-first search from index 0
        return dfs(0)
    
    def minExtraChar_using_trie(self, s: str, dictionary: List[str]) -> int:

        # Create a trie from the dictionary
        trie = Trie(dictionary)

        # Memoization dictionary to store the minimum extra characters for each index
        memo = {}

        def dfs(index):
            # Base case: if index reaches the end of the string, no extra characters are needed
            if index == len(s):
                return 0

            # If the result for this index is already computed, return it
            if index in memo:
                return memo[index]

            # Initialize the minimum extra characters to a large number
            min_extra_chars = float('inf')

            # Try to match each word in the dictionary with the substring starting at the current index
            node = trie.root
            for i in range(index, len(s)):
                if s[i] not in node.children:
                    break
                node = node.children[s[i]]
                if node.is_word:
                    min_extra_chars = min(min_extra_chars, dfs(i + 1))

            # Consider the case where the current character is an extra character
            min_extra_chars = min(min_extra_chars, 1 + dfs(index + 1))

            # Store the result in memoization dictionary
            memo[index] = min_extra_chars

            return min_extra_chars

        # Start the depth-first search from index 0
        return dfs(0)




sol = Solution()

print(sol.minExtraChar("leetscode", ["leet", "code", "leetcode"]))  # 1
print(sol.minExtraChar("sayhelloworld", ["hello", "world"]))  # 3
