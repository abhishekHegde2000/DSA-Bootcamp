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


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        i = 1

        # We want to get our i pointer (meaning curr becomes the resultant number) to k.
        # When we reach that, we will return that number.

        while i < k:
            # When i < k, we need to get the results till that array index,
            # but it's not possible to generate the entire array. So let's try another way.

            # Let's get the steps from each subtree starting at the current position, including the element itself.
            steps = self.count_children_of_subtree_at_given_position(curr, n)

            # Now, these steps will tell us how much we need to move -> either go to the next sibling or move down a level.

            if i + steps <= k:
                # This means there aren't enough child nodes present to reach the desired index.
                # We need to move to the immediate next subtree.
                curr += 1

                # In our DFS sorted array, we can skip that many indices. Suppose if we are at the 10th index
                # and the subtree contains 100 nodes, we can directly skip those and jump forward.
                i += steps
            else:
                # We are within the range, so we need to move down one level.
                curr *= 10

                # In our DFS tree, this means going down one level which moves by one index in the sorted array.
                i += 1

        return curr

    # How to get the number of child nodes between two siblings?
    # This is necessary because we are trying to skip entire subtrees.
    def count_children_of_subtree_at_given_position(self, curr, n):
        number_of_nodes = 0

        # We need to check the subtree starting from curr and its next neighbor.
        nei = curr + 1

        while curr <= n:
            # Make sure we don't exceed the total number range.
            nei = min(nei, n + 1)

            number_of_nodes += nei - curr

            # Move down to the next level in the tree.
            curr *= 10
            nei *= 10

        return number_of_nodes


sol = Solution()

print(sol.findKthNumber(13, 2))  # 10
print(sol.findKthNumber(1, 1))  # 1
print(sol.findKthNumber(100, 10))  # 10


class Solution(object):
    def findKthNumber(self, n, k):
        curr = 1
        k -= 1

        while k > 0:
            step = self._count_steps(n, curr, curr + 1)
            # If the steps are less than or equal to k, we skip this prefix's subtree
            if step <= k:
                # Move to the next prefix and decrease k by the number of steps we skip
                curr += 1
                k -= step
            else:
                # Move to the next level of the tree and decrement k by 1
                curr *= 10
                k -= 1

        return curr

    # To count how many numbers exist between prefix1 and prefix2
    def _count_steps(self, n, prefix1, prefix2):
        steps = 0
        while prefix1 <= n:
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10
        return steps
