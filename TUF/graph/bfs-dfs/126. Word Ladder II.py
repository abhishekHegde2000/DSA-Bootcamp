'''
https://leetcode.com/problems/word-ladder-ii/description/

126. Word Ladder II
Attempted
Hard
Topics
Companies
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
The sum of all shortest transformation sequences does not exceed 105.
'''

from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        # Append beginWord to wordList
        wordList.append(beginWord)

        # Create adjacency list for wildcard patterns
        adj = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                adj[pattern].append(word)

        # BFS initialization
        layers = {}
        layers[beginWord] = [[beginWord]]
        q = deque([beginWord])
        found = False

        while q and not found:
            next_layer = defaultdict(list)
            for _ in range(len(q)):
                word = q.popleft()
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neiWord in adj[pattern]:
                        if neiWord == endWord:
                            found = True
                        if neiWord not in layers:
                            next_layer[neiWord] += [path + [neiWord]
                                                    for path in layers[word]]
            layers.update(next_layer)
            q.extend(next_layer.keys())

        return layers.get(endWord, [])


# Example usage:
sol = Solution()
# [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
print(sol.findLadders("hit", "cog", [
      "hot", "dot", "dog", "lot", "log", "cog"]))
print(sol.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # []
print(sol.findLadders("hot", "dog", ["hot", "dog"]))  # []

