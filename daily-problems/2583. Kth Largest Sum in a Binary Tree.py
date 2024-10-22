'''
https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

2583. Kth Largest Sum in a Binary Tree
Medium
Topics
Companies
Hint
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

 

Example 1:


Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
Example 2:


Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= 106
1 <= k <= n
'''

# Definition for a binary tree node.

from typing import Optional
from collections import deque as Deque
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return -1

        q = Deque([root])
        pq = []

        while q:

            # Calculate level sum
            lvl_sum = 0
            size = len(q)

            for i in range(size):
                node = q.popleft()
                lvl_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Push level sum to max heap
            heapq.heappush(pq, -lvl_sum)
        
        # Check if k is greater than the number of levels
        if len(pq) < k:
            return -1
        
        # Pop the top k-1 elements from the max heap
        for i in range(k-1):
            heapq.heappop(pq)
        
        # Return the remaining top element (k-th largest level sum)
        return -heapq.heappop(pq)