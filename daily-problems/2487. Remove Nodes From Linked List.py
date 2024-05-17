'''
https://leetcode.com/problems/remove-nodes-from-linked-list/?envType=daily-question&envId=2024-05-06

2487. Remove Nodes From Linked List

You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
'''

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the previous node and the current node
        previous_node = None
        current_node = head

        while current_node:
            # Save the next node
            next_node = current_node.next
            print(f"next_node: {next_node.val if next_node else None}")

            # Reverse the link
            current_node.next = previous_node
            print(f"current_node.next: {
                  current_node.next.val if current_node.next else None}")

            # Move the previous node and the current node one step forward
            previous_node = current_node
            current_node = next_node
            print(f"previous_node: {previous_node.val if previous_node else None}, current_node: {
                  current_node.val if current_node else None}")

        # The head of the reversed list is the previous node
        return previous_node

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the list
        reversed_head = self.reverseList(head)

        # Initialize the current node, the maximum value, and the previous node
        current_node = reversed_head
        max_value = float('-inf')
        previous_node = None

        while current_node:
            # If the value of the current node is less than the maximum value, remove the current node from the list
            if current_node.val < max_value:
                previous_node.next = current_node.next
                print(f"previous_node.next: {
                      previous_node.next.val if previous_node.next else None}")
            # Otherwise, update the maximum value and move the previous node one step forward
            else:
                max_value = current_node.val
                print(f"max_value: {max_value}")
                previous_node = current_node
                print(f"previous_node: {
                      previous_node.val if previous_node else None}")

            # Move the current node one step forward
            current_node = current_node.next
            print(f"current_node: {
                  current_node.val if current_node else None}")

        # Reverse the list again to restore the original order
        return self.reverseList(reversed_head)


sol = Solution()

head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
print(sol.removeNodes(head))  # [13,8]

head = ListNode(1, ListNode(1, ListNode(1, ListNode(1))))
print(sol.removeNodes(head))  # [1,1,1,1]

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(sol.removeNodes(head))  # [5]
