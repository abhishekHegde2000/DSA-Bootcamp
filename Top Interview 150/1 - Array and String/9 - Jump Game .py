'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

'''

from typing import List

'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the maximum jump length
        max_jump_length = nums[0]
        print(f"Initial max jump length: {max_jump_length}")

        # Traverse all the elements in the list
        for i in range(1, len(nums)):
            # If the maximum jump length is 0, it means we can't jump to the current index
            if max_jump_length == 0:
                print(f"Can't jump to index {i}, returning False")
                return False

            # Decrement the maximum jump length
            max_jump_length -= 1
            print(f"Decrementing max jump length: {max_jump_length}")

            # Update the maximum jump length if the current number is greater
            max_jump_length = max(max_jump_length, nums[i])
            print(f"Updated max jump length: {max_jump_length}")

        # If we've gone through the whole list, it means we can reach the end
        print("Can reach the end, returning True")
        return True


# example usage
sol = Solution()
nums = [2, 3, 1, 1, 4]
print(sol.canJump(nums))
nums = [3, 2, 1, 0, 4]
print(sol.canJump(nums))

'''

'''

![image.png](https://assets.leetcode.com/users/images/822f9648-b4cd-40a7-8a26-79f2468a01c4_1703267716.065135.png)

 **Here's a breakdown of the code with explanations:**

**1. Initialization:**

- `max_jump_length = nums[0]`: Stores the maximum reachable index from the current position, starting with the first element's value.

**2. Iteration:**

- `for i in range(1, len(nums)):`: Loops through the array from the second element to the end.

**3. Checking for Reachable Positions:**

- `if max_jump_length == 0:`: If the maximum jump length is 0, it means you're stuck and can't reach further, so return `False`.

**4. Decrementing Jump Length:**

- `max_jump_length -= 1`: Decreases the maximum jump length by 1 after each jump.

**5. Updating Maximum Jump Length:**

- `max_jump_length = max(max_jump_length, nums[i])`: Updates `max_jump_length` with the maximum of its current value and the jump value at the current index, ensuring you always consider the farthest possible reach.

**6. Successful Traversal:**

- If the loop completes without encountering `max_jump_length == 0`, it means you can reach the end of the array, so return `True`.

**Key Points:**

- The code works backward, checking if you can reach each index from previous positions.
- It focuses on "obstacles" (zeros) that prevent direct jumps and uses a nested loop to find alternative paths if needed.
- It maintains `max_jump_length` to track the farthest reachable index, optimizing the traversal.

**Time Complexity:** O(n), where n is the length of the array.
**Space Complexity:** O(1), using constant extra space.


# Code
```
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the maximum jump length
        max_jump_length = nums[0]
        print(f"Initial max jump length: {max_jump_length}")

        # Traverse all the elements in the list
        for i in range(1, len(nums)):
            # If the maximum jump length is 0, it means we can't jump to the current index
            if max_jump_length == 0:
                print(f"Can't jump to index {i}, returning False")
                return False

            # Decrement the maximum jump length
            max_jump_length -= 1
            print(f"Decrementing max jump length: {max_jump_length}")

            # Update the maximum jump length if the current number is greater
            max_jump_length = max(max_jump_length, nums[i])
            print(f"Updated max jump length: {max_jump_length}")

        # If we've gone through the whole list, it means we can reach the end
        print("Can reach the end, returning True")
        return True
```

'''

'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Get the length of the input array
        array_length = len(nums)
        print(f"Array length: {array_length}")

        # Initialize a boolean array to track reachable positions
        reachable_positions = [False] * array_length
        print(f"Initial reachable positions: {reachable_positions}")

        # The first position is always reachable
        reachable_positions[0] = True

        # Traverse the array
        for i in range(array_length):
            print(f"Checking position {i}")
            # If the current position is reachable
            if reachable_positions[i]:
                print(f"Position {i} is reachable")
                # Update the reachable positions based on the maximum jump length
                for j in range(1, nums[i] + 1):
                    if i + j < array_length:
                        reachable_positions[i + j] = True
                        print(
                            f"Updated reachable positions: {reachable_positions}")
                    if i + j == array_length - 1:
                        print("Can reach the last position, returning True")
                        return True

        # Return the reachability of the last position
        print(
            f"Can reach the last position: {reachable_positions[array_length - 1]}")
        return reachable_positions[array_length - 1]

'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the target index to the last index of the list
        target_index = len(nums) - 1
        print(f"Initial target index: {target_index}")

        # Traverse the list in reverse order
        for i in range(len(nums) - 2, -1, -1):
            print(f"Checking index {i} with value {nums[i]}")
            # If the current index plus the value at this index is greater than or equal to the target index
            if i + nums[i] >= target_index:
                # Update the target index to the current index
                target_index = i
                print(f"Updated target index: {target_index}")

        # If the target index is 0, it means we can reach the end of the list
        print(f"Final target index: {target_index}")
        return target_index == 0


# example usage
sol = Solution()
nums = [2, 3, 1, 1, 4]
print(sol.canJump(nums))
nums = [3, 2, 1, 0, 4]
print(sol.canJump(nums))
