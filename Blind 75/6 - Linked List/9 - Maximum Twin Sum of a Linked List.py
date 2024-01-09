'''
2130. Maximum Twin Sum of a Linked List

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Reverse the first half of the linked list
        slow_pointer, fast_pointer = head, head
        previous_node = None
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            next_node = slow_pointer.next
            slow_pointer.next = previous_node
            previous_node = slow_pointer
            slow_pointer = next_node

        # Debugging print statement
        print(f"Reversed the first half of the linked list")

        # Step 2: Initialize two pointers at the start of the reversed first half and the second half
        reversed_first_half_node, second_half_node = previous_node, slow_pointer

        # Step 3: Initialize variables for the maximum sum and the current sum
        max_sum, current_sum = 0, 0

        # Step 4: Traverse the two halves together
        while second_half_node:
            # For each pair of nodes, update the current sum and the maximum sum
            current_sum = reversed_first_half_node.val + second_half_node.val
            max_sum = max(max_sum, current_sum)

            # Debugging print statement
            print(f"Updated the current sum and the maximum sum")

            reversed_first_half_node = reversed_first_half_node.next
            second_half_node = second_half_node.next

        # Step 5: Return the maximum sum
        return max_sum
