'''
https://leetcode.com/problems/merge-two-sorted-lists/

Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 


'''
from typing import Optional, List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Initialize a dummy node and a tail node pointing to the dummy node
        dummy_node = ListNode()
        tail_node = dummy_node

        # Step 2: While both lists are not empty, compare the first node of each list, append the smaller node to the tail node, and move the pointer of the smaller node to the next node
        while list1 and list2:
            if list1.val < list2.val:
                tail_node.next = list1
                list1 = list1.next
            else:
                tail_node.next = list2
                list2 = list2.next
            tail_node = tail_node.next

        # Step 3: If one list becomes empty before the other, append the remaining nodes of the non-empty list to the tail node
        if list1:
            tail_node.next = list1
        else:
            tail_node.next = list2

        # Step 4: Return the next node of the dummy node, which is the head node of the new list
        return dummy_node.next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # If either of the lists is empty, return the other list
        if not list1:
            return list2
        if not list2:
            return list1

        # Compare the values of the first nodes of the two lists
        if list1.val < list2.val:
            print(f"Node with value {list1.val} from list1 is smaller")
            # Set the next pointer of the smaller node to the result of the recursive call with the next node of the smaller list and the other list
            list1.next = self.mergeTwoLists(list1.next, list2)
            # Return the smaller node
            return list1
        else:
            print(f"Node with value {list2.val} from list2 is smaller")
            # Set the next pointer of the smaller node to the result of the recursive call with the next node of the smaller list and the other list
            list2.next = self.mergeTwoLists(list1, list2.next)
            # Return the smaller node
            return list2


sol = Solution()
print(sol.mergeTwoLists([1, 2, 4], [1, 3, 4]))
print(sol.mergeTwoLists([], []))
print(sol.mergeTwoLists([], [0]))
