'''
https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150

228. Summary Ranges

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.

'''


class Solution:
    def summaryRanges(self, nums):
        # Check if nums is empty
        if not nums:
            return []

        # Initialize ranges and start
        ranges = []
        start = nums[0]
        print(f"Initial start: {start}")

        # Iterate over nums from the second number to the last number
        for i in range(1, len(nums)):
            print(f"Current number: {nums[i]}, start: {start}")

            # If the current number is not equal to the previous number plus 1
            if nums[i] != nums[i-1] + 1:
                print(f"Range ended at {nums[i-1]}")

                # If start is equal to the previous number
                if start == nums[i-1]:
                    ranges.append(str(start))
                # If start is not equal to the previous number
                else:
                    ranges.append(str(start) + "->" + str(nums[i-1]))

                print(f"Ranges: {ranges}")

                # Set start to be the current number
                start = nums[i]

        print(f"Final start: {start}")

        # Handle the last range
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(nums[-1]))

        print(f"Final ranges: {ranges}")

        return ranges


sol = Solution()

print(sol.summaryRanges([0, 1, 2, 4, 5, 7]))  # ["0->2","4->5","7"]
print(sol.summaryRanges([0, 2, 3, 4, 6, 8, 9]))  # ["0","2->4","6","8->9"]
print(sol.summaryRanges([0]))  # ["0"]
print(sol.summaryRanges([]))  # []
print(sol.summaryRanges([1]))  # ["1"]
