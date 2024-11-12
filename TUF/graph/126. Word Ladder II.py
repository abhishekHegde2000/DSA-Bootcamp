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


from collections import deque


class Solution:
    def bfs(self, endWord, wordset, wordList, queue, levelmap):
        length = len(queue)
        for _ in range(length):
            u = queue.popleft()
            curr = u[0]
            if curr == endWord:
                return levelmap
            else:
                for word in wordList:
                    count = 0
                    for i in range(len(curr)):
                        if word[i] != curr[i]:
                            count += 1

                    if count == 1 and (word in wordset):
                        queue.append([word, u[1]+1])
                        wordset.remove(word)
                        levelmap[word] = u[1]+1

        if queue:
            # for w in queue:
            #     wordset.discard(w[0])
            return self.bfs(endWord, wordset, wordList, queue, levelmap)
        else:
            return levelmap

    def dfs(self, endWord, beginWord, levelmap):
        if endWord == beginWord:
            return [[beginWord]]
        level = levelmap[endWord] - 1
        trans = []
        for k in levelmap.keys():
            if levelmap[k] == level:
                count = 0
                for i in range(len(endWord)):
                    if k[i] != endWord[i]:
                        count += 1
                if count == 1:
                    result = self.dfs(k, beginWord, levelmap)
                    for i in range(len(result)):
                        result[i].append(endWord)
                        trans.append(result[i])

        return trans

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        rows = len(wordList)
        if rows > 0:
            cols = len(wordList[0])

        if endWord not in wordList:
            return []
        if endWord == beginWord:
            return [beginWord]

        queue = deque()
        queue.append([beginWord, 0])
        # original_wordset = wordset
        wordset = set(wordList)
        wordset.discard(beginWord)
        levelmap = {}
        levelmap[beginWord] = 0
        levelmap = self.bfs(endWord, wordset, wordList, queue, levelmap)
        # return levelmap
        if len(levelmap) == 1 or (levelmap.get(endWord) is None):
            return []

        all_trans = self.dfs(endWord, beginWord, levelmap)
        return all_trans
