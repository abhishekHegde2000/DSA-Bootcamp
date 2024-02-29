'''

https://leetcode.com/problems/reorder-list/

143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 
 
 '''


from typing import Optional, List
from typing import Optional, List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev, curr = None, slow.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Merge the two halves of the list
        slow.next = None  # break the link between the two halves

        first, second = head, prev
        while second:
            next_node = first.next
            first.next = second
            first = second
            second = next_node

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         if not head:
#             return

#         # Step 1: Traverse the linked list and store each node into an array
#         arr = []
#         node = head
#         while node:
#             arr.append(node)
#             node = node.next

#         # Step 2: Use two pointers, one starting from the beginning of the array and the other from the end
#         i, j = 0, len(arr) - 1

#         # Step 3: Connect the nodes based on the pointers and continue this process until the pointers meet
#         while i < j:
#             # Connect the nodes
#             arr[i].next = arr[j]
#             i += 1

#             # If pointers have met then break
#             if i == j:
#                 break

#             # Connect the nodes
#             arr[j].next = arr[i]
#             j -= 1

#         # Step 4: Make sure to set the next of the last node to None to avoid any cycles in the list
#         arr[i].next = None


sol = Solution()
print(sol.reorderList([1, 2, 3, 4, 5]))  # [1, 5, 2, 4, 3]
print(sol.reorderList([1, 2, 3, 4]))  # [1, 4, 2, 3]
print(sol.reorderList([1, 2, 3]))
print(sol.reorderList([1, 2]))
print(sol.reorderList([1]))
print(sol.reorderList([]))
