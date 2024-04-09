'''
https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

1171. Remove Zero Sum Consecutive Nodes from Linked List

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.

'''


from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum_to_node = {}
        prefix_sum = 0
        current = dummy

        while current:
            prefix_sum += current.val

            # If the current prefix sum is in the dictionary, remove consecutive nodes with a sum of 0
            if prefix_sum in prefix_sum_to_node:
                prev = prefix_sum_to_node[prefix_sum]
                to_remove = prev.next
                p = prefix_sum + (to_remove.val if to_remove else 0)

                while p != prefix_sum:
                    del prefix_sum_to_node[p]
                    to_remove = to_remove.next
                    p += to_remove.val if to_remove else 0

                prev.next = current.next
            else:
                prefix_sum_to_node[prefix_sum] = current

            current = current.next

        return dummy.next


# Test Case 1
# Input: [1, 2, -3, 3, 1]
# After removing consecutive nodes with a sum of 0: [3, 1]
assert Solution().removeZeroSumSublists(ListNode(1, ListNode(
    2, ListNode(-3, ListNode(3, ListNode(1)))))).to_list() == [3, 1]

# Test Case 2
# Input: [1, 2, 3, -3, 4]
# After removing consecutive nodes with a sum of 0: [1, 2, 4]
assert Solution().removeZeroSumSublists(ListNode(1, ListNode(
    2, ListNode(3, ListNode(-3, ListNode(4)))))).to_list() == [1, 2, 4]

# Test Case 3
# Input: [1, 2, 3, -3, -2]
# After removing consecutive nodes with a sum of 0: [1]
assert Solution().removeZeroSumSublists(ListNode(1, ListNode(
    2, ListNode(3, ListNode(-3, ListNode(-2)))))).to_list() == [1]

# Test Case 4
# Input: [1, 2, 3]
# After removing consecutive nodes with a sum of 0: [1, 2, 3]
assert Solution().removeZeroSumSublists(
    ListNode(1, ListNode(2, ListNode(3)))).to_list() == [1, 2, 3]

# Test Case 5
# Input: [1, -1]
# After removing consecutive nodes with a sum of 0: []
assert Solution().removeZeroSumSublists(
    ListNode(1, ListNode(-1))).to_list() == []
