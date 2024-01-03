'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

![image.png](https://assets.leetcode.com/users/images/7ab42412-aaee-4fdc-baa7-15dc5e7c9fc2_1703340919.4830198.png)

'''

from typing import List


'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get the length of the input list
        num_length = len(nums)
        # Initialize an output list with the same length as the input list
        output = [0] * num_length

        # Iterate over each number in the input list
        for i in range(num_length):
            # Initialize the product of all other numbers as 1
            product_of_others = 1
            # Iterate over each number in the input list again
            for j in range(num_length):
                # Skip the number at the current index
                if j == i:
                    continue
                # Multiply the product of all other numbers by the current number
                product_of_others *= nums[j]
            # Print the product of all other numbers
            print(
                f"Product of all numbers except nums[{i}]: {product_of_others}")
            # Store the product of all other numbers in the output list
            output[i] = product_of_others

        # Return the output list
        return output

'''


'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get the length of the input list
        num_length = len(nums)
        # Initialize an output list with the same length as the input list
        output = [0] * num_length
        # Initialize the prefix product as 1
        prefix_product = 1

        # Calculate the prefix product for each number
        for i in range(num_length):
            # Store the prefix product in the output list
            output[i] = prefix_product
            # Update the prefix product
            prefix_product *= nums[i]
            # Print the prefix product
            print(f"Prefix product for nums[{i}]: {prefix_product}")

        # Initialize the postfix product as 1
        postfix_product = 1

        # Calculate the postfix product for each number
        for i in range(num_length - 1, -1, -1):
            # Multiply the postfix product with the corresponding element in the output list
            output[i] *= postfix_product
            # Update the postfix product
            postfix_product *= nums[i]
            # Print the postfix product
            print(f"Postfix product for nums[{i}]: {postfix_product}")

        # Return the output list
        return output

'''


'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Calculate the total product of all numbers
        total_product = 1
        for num in nums:
            total_product *= num

        # Create an output array where each element is the total product divided by the corresponding number
        output = [total_product // num for num in nums]

        return output

'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get the length of the input list
        num_length = len(nums)
        # Initialize an output list with the same length as the input list
        output = [0] * num_length
        # Initialize the prefix product as 1
        prefix_product = 1

        # Calculate the prefix product for each number
        for i in range(num_length):
            # Store the prefix product in the output list
            output[i] = prefix_product
            # Update the prefix product
            prefix_product *= nums[i]
            # Print the prefix product
            print(f"Prefix product for nums[{i}]: {prefix_product}")

        # Initialize the postfix product as 1
        postfix_product = 1

        # Calculate the postfix product for each number
        for i in range(num_length - 1, -1, -1):
            # Multiply the postfix product with the corresponding element in the output list
            output[i] *= postfix_product
            # Update the postfix product
            postfix_product *= nums[i]
            # Print the postfix product
            print(f"Postfix product for nums[{i}]: {postfix_product}")

        # Return the output list
        return output


sol = Solution()
nums = [1, 2, 3, 4]
print(sol.productExceptSelf(nums))
nums = [-1, 1, 0, -3, 3]
print(sol.productExceptSelf(nums))
