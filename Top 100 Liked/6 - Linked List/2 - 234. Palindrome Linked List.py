'''
https://leetcode.com/problems/palindrome-linked-list

234. Palindrome Linked List


Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
'''

from typing import Optional

# Definition for singly-linked list.
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = self.middle(head)
        end = self.reverse(middle)
        return self.palidrome(head, end)

    def middle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, slow):
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def palidrome(self, head, prev):
        first, second = head, prev
        while second:
            if second.val != first.val:
                return False
            first = first.next
            second = second.next
        return True


# Define ListNode values for dummy cases
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)
node_6 = ListNode(6)

# Connect ListNodes to form linked lists
node_1.next = node_2
node_2.next = node_3
node_3.next = node_2  # Palindrome list
node_4.next = node_5
node_5.next = node_6

# Create an instance of the Solution class
sol = Solution()

# Test cases
print(sol.isPalindrome(node_1))   # Output: True (Palindrome) [1,2,2,1]
print(sol.isPalindrome(node_4))  # Output: False (Non-Palindrome) [4,5,6]


# Define ListNode values for additional dummy cases
node_7 = ListNode(1)
node_8 = ListNode(2)
node_9 = ListNode(3)
node_10 = ListNode(2)
node_11 = ListNode(1)
node_12 = ListNode(4)

# Connect ListNodes to form linked lists
node_7.next = node_8
node_8.next = node_9
node_9.next = node_10
node_10.next = node_11
node_12.next = None

# Test case with an odd-length palindrome list
print(sol.isPalindrome(node_7))  # Output: True (Odd-length palindrome)
