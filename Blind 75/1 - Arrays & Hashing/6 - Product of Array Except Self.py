'''
product of array except self

https://leetcode.com/problems/product-of-array-except-self/

238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get the length of the input list
        num_length = len(nums)
        # Initialize prefix and suffix product lists
        prefix_products = [1] * num_length
        suffix_products = [1] * num_length

        # Calculate the prefix products
        for i in range(1, num_length):
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1]
            print(f"Prefix products: {prefix_products}")

        # Calculate the suffix products
        for i in range(num_length - 2, -1, -1):
            suffix_products[i] = suffix_products[i + 1] * nums[i + 1]
            print(f"Suffix products: {suffix_products}")

        # Initialize the output list
        output = [0] * num_length
        # Calculate the product of the prefix and suffix products for each number
        for i in range(num_length):
            output[i] = prefix_products[i] * suffix_products[i]
            print(f"Output: {output}")

        # Return the output list
        return output


class Solution1:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
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
