'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
'''


from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers: one for the previous node and one for the current node
        previousNode, currentNode = None, head

        # Iterate over the linked list
        while currentNode:
            # Store the next node
            nextNode = currentNode.next
            print(f"Stored next node: {nextNode.val if nextNode else 'None'}")

            # Update the next pointer of the current node to the previous node
            currentNode.next = previousNode
            print(f"Updated next pointer of current node: {
                  currentNode.val if currentNode else 'None'}")

            # Update the previous node to the current node
            previousNode = currentNode
            print(f"Updated previous node: {
                  previousNode.val if previousNode else 'None'}")

            # Update the current node to the next node
            currentNode = nextNode
            print(f"Updated current node: {
                  currentNode.val if currentNode else 'None'}")

        # After the end of the loop, the previous node will be the new head of the reversed linked list
        return previousNode

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the head node or the next node is None, return the head node
        if not head or not head.next:
            return head

        # Reverse the rest of the list
        newHead = self.reverseList(head.next)
        print(f"Reversed the rest of the list: {
              newHead.val if newHead else 'None'}")

        # Update the next pointer of the next node to the current node
        head.next.next = head
        print(f"Updated next pointer of next node: {
              head.next.val if head.next else 'None'}")

        # Update the next pointer of the current node to None
        head.next = None
        print(f"Updated next pointer of current node: {
              head.val if head else 'None'}")

        # Return the new head of the reversed linked list
        return newHead


sol = Solution()
print(sol.reverseList([1, 2, 3, 4, 5]))
print(sol.reverseList([1, 2]))
print(sol.reverseList([]))
