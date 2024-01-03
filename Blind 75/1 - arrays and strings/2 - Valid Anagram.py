'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

'''
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        a = Counter(s)
        b = Counter(t)

        return a == b


sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))
s = "rat"
t = "car"
print(sol.isAnagram(s, t))
