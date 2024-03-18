'''
https://leetcode.com/problems/linked-list-cycle/

141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

'''

from typing import Optional, List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Step 1: Initialize two pointers at the head of the list
        slow_pointer, fast_pointer = head, head

        # Debugging print statement
        print(f"Initialized slow_pointer and fast_pointer at the head of the list")

        # Step 2: Move the slow pointer one step at a time and the fast pointer two steps at a time
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            # Debugging print statement
            print(f"Moved slow_pointer one step and fast_pointer two steps")

            # Step 3: If the slow pointer and the fast pointer meet, there is a cycle in the list
            if slow_pointer == fast_pointer:
                # Debugging print statement
                print(f"Detected a cycle in the list")
                return True

        # Step 4: If the fast pointer reaches the end of the list, there is no cycle
        # Debugging print statement
        print(f"No cycle detected in the list")
        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Step 1: Initialize a hash map
        node_map = {}

        # Debugging print statement
        print(f"Initialized an empty hash map")

        # Step 2: Traverse the list
        while head:
            # Step 3: If the node is in the hash map, return True because we have a cycle
            if head in node_map:
                # Debugging print statement
                print(f"Detected a cycle in the list")
                return True

            # Step 4: If the node is not in the hash map, add it to the hash map and continue to the next node
            else:
                node_map[head] = 1
                # Debugging print statement
                print(f"Added a new node to the hash map")

            head = head.next

        # Step 5: If we reach the end of the list, return False because there is no cycle
        # Debugging print statement
        print(f"No cycle detected in the list")
        return False
