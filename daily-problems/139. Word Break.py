'''
https://leetcode.com/problems/word-break/description/


139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize a memoization dictionary
        memo = {}

        def backtrack(start_index):
            print(f"\nProcessing index {start_index}")

            # If the starting index is in the memo, return the stored result
            if start_index in memo:
                print(f"Found {start_index} in memo with result {
                      memo[start_index]}")
                return memo[start_index]

            # If the starting index is equal to the length of s, return True
            if start_index == len(s):
                print(f"Reached the end of the string at index {start_index}")
                return True

            # Iterate over each word in the word dictionary
            for word in wordDict:
                print(f"Checking word {word} at index {start_index}")

                # If the substring of s starting at the current index is equal to the current word
                if s.startswith(word, start_index):
                    print(f"Found word {word} at index {start_index}")

                    # Recursively call backtrack with the new starting index
                    if backtrack(start_index + len(word)):
                        print(f"Returning True from index {start_index}")

                        # Store the result in the memo and return True
                        memo[start_index] = True
                        return True

            print(f"No word found at index {start_index}")

            # If no word in the dictionary matches the substring of s starting at the current index
            # Store the result in the memo and return False
            memo[start_index] = False
            return False

        # Call backtrack with a starting index of 0
        return backtrack(0)


sol = Solution()

print(sol.wordBreak("leetcode", ["leet", "code"]))  # True
print(sol.wordBreak("applepenapple", ["apple", "pen"]))  # True
print(sol.wordBreak("catsandog", [
      "cats", "dog", "sand", "and", "cat"]))  # False
