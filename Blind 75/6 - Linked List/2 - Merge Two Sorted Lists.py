'''
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
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next


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
