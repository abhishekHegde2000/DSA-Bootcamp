'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Initialize a dummy node and a tail node pointing to the dummy node
        dummy_node = ListNode()
        current_node = dummy_node

        # Debugging print statement
        print(f"Initialized a dummy node and a current node pointing to the dummy node")

        # Step 2: Initialize a carry variable
        carry = 0

        # Debugging print statement
        print(f"Initialized a carry variable")

        # Step 3: While both lists are not empty, add the values of the two nodes and the carry, and append the sum to the current node
        while l1 or l2 or carry:
            # If the first list is not empty, add the value of the first node to the carry and move the pointer to the next node
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total_value = val1 + val2 + carry

            carry = total_value // 10
            node_value = total_value % 10

            current_node.next = ListNode(node_value)
            current_node = current_node.next

            # Debugging print statement
            print(
                f"Added the values of the two nodes and the carry, and appended the sum to the current node")

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Step 4: Return the next node of the dummy node
        return dummy_node.next
