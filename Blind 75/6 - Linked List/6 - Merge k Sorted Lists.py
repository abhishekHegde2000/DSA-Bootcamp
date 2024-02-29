'''
https://leetcode.com/problems/merge-k-sorted-lists/

23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

from typing import Optional, List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Step 1: If the input list is empty or contains no lists, return None
        if not lists or len(lists) == 0:
            return None

        # Step 2: If the input list contains only one list, return that list
        if len(lists) == 1:
            return lists[0]

        # Step 3: Define a function to merge two lists
        def mergeTwoLists(list1, list2):
            dummyNode = ListNode()
            currentNode = dummyNode
            while list1 and list2:
                if list1.val < list2.val:
                    currentNode.next = list1
                    list1 = list1.next
                else:
                    currentNode.next = list2
                    list2 = list2.next
                currentNode = currentNode.next

            if list1:
                currentNode.next = list1
            else:
                currentNode.next = list2

            return dummyNode.next

        # Debugging print statement
        print(f"Initialized mergeTwoLists function")

        # Step 4: While there is more than one list in the input list, merge the lists two at a time and add the merged lists to a new list
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(mergeTwoLists(list1, list2))

            # Debugging print statement
            print(f"Merged {len(lists)} lists into {len(mergedLists)} lists")

            # Step 5: Replace the input list with the new list
            lists = mergedLists

        # Step 6: Repeat steps 4 and 5 until there is only one list left in the input list
        # Step 7: Return the remaining list
        return lists[0]


sol = Solution()
print(sol.mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]]))
print(sol.mergeKLists([]))
print(sol.mergeKLists([[]]))
