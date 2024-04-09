'''
https://leetcode.com/problems/odd-even-linked-list/


328. Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
'''
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: If the list is empty or has only one node, return the list as it is
        if not head or not head.next:
            return head

        # Step 2: Initialize two pointers at the head of the list and a variable to keep track of the first even node
        odd_pointer = head
        even_pointer = head.next
        first_even_node = even_pointer

        # Debugging print statement
        print(f"Initialized odd_pointer, even_pointer, and first_even_node at the head of the list")

        # Step 3: Traverse the list
        while even_pointer and even_pointer.next:
            # For each node, if it is an odd node, connect it to the next odd node
            odd_pointer.next = even_pointer.next
            odd_pointer = odd_pointer.next

            # If it is an even node, connect it to the next even node
            even_pointer.next = odd_pointer.next
            even_pointer = even_pointer.next

            # Debugging print statement
            print(
                f"Connected odd_pointer to the next odd node and even_pointer to the next even node")

        # Step 4: After traversing the list, connect the last odd node to the first even node
        odd_pointer.next = first_even_node

        # Debugging print statement
        print(f"Connected the last odd node to the first even node")

        return head
