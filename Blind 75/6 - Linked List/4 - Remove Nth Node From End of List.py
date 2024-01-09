'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?

'''

from typing import Optional, List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Initialize a dummy node and two pointers at the dummy node
        dummy_node = ListNode(0)
        dummy_node.next = head
        first_pointer = dummy_node
        second_pointer = dummy_node

        # Debugging print statement
        print(f"Initialized dummy node and two pointers at the dummy node")

        # Step 2: Move the first pointer n nodes ahead
        for i in range(n + 1):
            first_pointer = first_pointer.next

        # Debugging print statement
        print(f"Moved the first pointer {n} nodes ahead")

        # Step 3: Move both pointers one step at a time until the first pointer reaches the end of the list
        while first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        # Debugging print statement
        print(f"Moved both pointers one step at a time until the first pointer reached the end of the list")

        # Step 4: The second pointer will now be at the nth node from the end. Remove the nth node
        second_pointer.next = second_pointer.next.next

        # Debugging print statement
        print(f"Removed the nth node from the end")

        # Step 5: Return the next node of the dummy node, which is the head node of the new list
        return dummy_node.next


sol = Solution()
print(sol.removeNthFromEnd(head=[1, 2, 3, 4, 5], n=2))
print(sol.removeNthFromEnd(head=[1], n=1))
print(sol.removeNthFromEnd(head=[1, 2], n=1))


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Function to reverse a linked list
        def reverse(node):
            previous_node = None
            while node:
                next_node = node.next
                node.next = previous_node
                previous_node = node
                node = next_node
            return previous_node

        # Function to remove the nth node from the start of a linked list
        def removeNthFromStart(head, n):
            dummy_node = ListNode(0)
            dummy_node.next = head
            current_node = dummy_node
            for _ in range(n - 1):
                if current_node.next:  # Ensure that the current_node isn't None before moving forward
                    current_node = current_node.next
            if current_node.next:  # Ensure that the current_node isn't None before trying to access its 'next' attribute
                current_node.next = current_node.next.next
            return dummy_node.next

        # Debugging print statement
        print(f"Initial list: {head}")

        # Step 1: Reverse the list
        head = reverse(head)

        # Debugging print statement
        print(f"List after reversing: {head}")

        # Step 2: Remove the nth node from the start
        head = removeNthFromStart(head, n)

        # Debugging print statement
        print(f"List after removing the nth node from the start: {head}")

        # Step 3: Reverse the list again
        head = reverse(head)

        # Debugging print statement
        print(f"Final list: {head}")

        return head
