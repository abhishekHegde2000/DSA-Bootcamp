'''
https://leetcode.com/problems/swap-nodes-in-pairs/

24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''
from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        while curr and curr.next:
            # save nextpair and second node
            # 1 - 2 - 3 , 3 should be next pair , 2 should be wsecond pair
            nextPair = curr.next.next
            # 1 is at current so second should be 2
            second = curr.next

            # swap the position
            second.next = curr
            # prev is pointing to 1 , but now that we have changed the position,
            prev.next = second
            # 1 is still pooint to 2 so its next should point to 3
            curr.next = nextPair

            # the swap starts from nextPair, so at 3 we should begin
            prev = curr
            curr = nextPair

        return dummy.next
