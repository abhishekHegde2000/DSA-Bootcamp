'''
https://leetcode.com/problems/word-ladder/

127. Word Ladder
Solved
Hard
Topics
Companies
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1.2M
Submissions
2.9M
Acceptance Rate
40.8%
Topics
Hash Table
String
Breadth-First Search
'''


from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Append beginWord to wordList
        wordList.append(beginWord)

        # Create adjacency list for wildcard patterns
        adj = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                adj[pattern].append(word)

        # BFS initialization
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            size = len(q)
            for _ in range(size):
                word = q.popleft()
                if word == endWord:
                    return res

                # Generate wildcard patterns for current word
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neiWord in adj[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)

            res += 1

        return 0  # If no transformation sequence found


sol = Solution()

print(sol.ladderLength("hit", "cog", [
      "hot", "dot", "dog", "lot", "log", "cog"]))  # 5
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
print(sol.ladderLength("hot", "dog", ["hot", "dog"]))  # 0
