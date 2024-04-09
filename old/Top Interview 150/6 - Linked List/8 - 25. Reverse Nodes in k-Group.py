'''
https://leetcode.com/problems/reverse-nodes-in-k-group/

25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
'''

from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # lets create  a dummy node with dummy.next set to heed
        dummy = ListNode(0, head)
        # 1 -> | 2 -> 3 | similar to this why we have a previous node
        # 1 - > 3 - > 2
        nodeBeforeGroup = dummy

        while True:
            kth = self.getKth(k, nodeBeforeGroup)  # thing of it as 2
            if not kth:
                break
            # suppose if 2 -> 1 happended , we need to save 3 to get 1 -> 3
            nodeAfterGroup = kth.next  # currently think of it as 3

            # lets reverse the group now
            prev, curr = nodeAfterGroup, nodeBeforeGroup.next

            while curr != nodeAfterGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp = nodeBeforeGroup.next
            nodeBeforeGroup.next = kth
            nodeBeforeGroup = tmp
        return dummy.next

    # this function is written to determine if we readed the end of the group then we need to get the kth node
    # suppor in about example we use 3 -> 2 , how we get 3 is by looping till kth node since k is 2 hear and we will start from 1, it goes till 3
    def getKth(self, k, prev_node):

        while prev_node and k > 0:
            prev_node = prev_node.next
            k -= 1
        # suppose we dont have a node it will return None
        return prev_node


sol = Solution()

# Example 1
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
head = sol.reverseKGroup(head, k)  # [2,1,4,3,5]

# Example 2
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 3
head = sol.reverseKGroup(head, k)  # [3,2,1,4,5]

# Example 3
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 1
head = sol.reverseKGroup(head, k)  # [1,2,3,4,5]
