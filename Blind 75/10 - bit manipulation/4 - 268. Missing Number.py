'''
https://leetcode.com/problems/missing-number/description/ 

268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
 

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?


'''
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Initialize a variable to hold the missing number.
        missing_number = 0

        # Iterate over the range from 0 to the length of the input array.
        for i in range(len(nums)):

            # Update the missing number by performing a bitwise XOR operation between the current index and the current element.
            missing_number ^= i ^ nums[i]

        # Perform a bitwise XOR operation between the missing number and the length of the input array.
        missing_number ^= len(nums)

        # Return the missing number.
        return missing_number


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        s = sum(nums)
        n = len(nums)
        s1 = (n * (n + 1)) // 2
        return s1 - s


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # binary Search
        nums.sort()

        print(f"nums = {nums}")
        if nums[0] != 0:
            return 0

        n = len(nums)

        left, right = 0, n-1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1

        return left


sol = Solution()
print(sol.missingNumber([1, 4, 3, 2]))  # 0
print(sol.missingNumber([3, 0, 1]))  # 2
print(sol.missingNumber([0, 1]))  # 2
print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
