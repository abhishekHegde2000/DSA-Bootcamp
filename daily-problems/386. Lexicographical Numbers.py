'''
https://leetcode.com/problems/lexicographical-numbers/description/


386. Lexicographical Numbers
Medium
Topics
Companies
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104
'''
from typing import List


class TreeNode:

    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self, n):
        self.data = [str(i) for i in range(1, n + 1)]
        self.root = TreeNode()
        self.insert()

    def insert(self):
        for num in self.data:
            node = self.root
            for digit in num:
                if digit not in node.children:
                    node.children[digit] = TreeNode()
                node = node.children[digit]
            node.word = True


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        trie = Trie(n)
        result = []

        def dfs(node, num):
            if node.word:
                result.append(int(num))
            for child in sorted(node.children.keys()):
                dfs(node.children[child], num + child)

        dfs(trie.root, '')
        return result 


