'''
https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/

440. K-th Smallest in Lexicographical Order

Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 109
'''


class TreeNode:
    def __init__(self):
        self.children = []
        self.word = False


class Trie:
    def __init__(self, n: int):
        self.root = TreeNode()
        self.n = n
        
    
    def insert(self, num: int):
        node = self.root
        for i in range(self.n):
            if not node.children:
                node.children = [TreeNode() for _ in range(10)]
            node = node.children[num % 10]
            num //= 10
        node.word = True


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        pass


sol = Solution()

print(sol.findKthNumber(13, 2))  # 10
print(sol.findKthNumber(1, 1))  # 1
print(sol.findKthNumber(100, 10))  # 10
