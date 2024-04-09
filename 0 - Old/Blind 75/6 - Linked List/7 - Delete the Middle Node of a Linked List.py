'''
https://leetcode.com/problems/delete-middle-node-of-a-linked-list/

2095. Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
 

Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105
'''


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: If the list has only one node, return None because there is no middle node to delete
        if not head.next:
            return None

        # Step 2: Initialize two pointers at the head of the list and a variable to keep track of the previous node
        slow_pointer, fast_pointer = head, head
        previous_node = None

        # Debugging print statement
        print(f"Initialized slow_pointer, fast_pointer, and previous_node at the head of the list")

        # Step 3: Move the slow pointer one step at a time and the fast pointer two steps at a time
        while fast_pointer and fast_pointer.next:
            previous_node = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            # Debugging print statement
            print(f"Moved slow_pointer one step and fast_pointer two steps")

        # Step 4: When the fast pointer reaches the end of the list, the slow pointer will be at the middle of the list
        # Update the next pointer of the previous node to skip the middle node
        previous_node.next = slow_pointer.next

        # Debugging print statement
        print(f"Updated the next pointer of previous_node to skip the middle node")

        # Step 5: Delete the middle node
        del slow_pointer

        # Debugging print statement
        print(f"Deleted the middle node")

        return head
