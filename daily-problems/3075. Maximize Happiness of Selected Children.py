'''
https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

3075. Maximize Happiness of Selected Children

You are given an array happiness of length n, and a positive integer k.

There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.

In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

 

Example 1:

Input: happiness = [1,2,3], k = 2
Output: 4
Explanation: We can pick 2 children in the following way:
- Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
- Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
The sum of the happiness values of the selected children is 3 + 1 = 4.
Example 2:

Input: happiness = [1,1,1,1], k = 2
Output: 1
Explanation: We can pick 2 children in the following way:
- Pick any child with the happiness value == 1. The happiness value of the remaining children becomes [0,0,0].
- Pick the child with the happiness value == 0. The happiness value of the remaining child becomes [0,0].
The sum of the happiness values of the selected children is 1 + 0 = 1.
Example 3:

Input: happiness = [2,3,4,5], k = 1
Output: 5
Explanation: We can pick 1 child in the following way:
- Pick the child with the happiness value == 5. The happiness value of the remaining children becomes [1,2,3].
The sum of the happiness values of the selected children is 5.
 

Constraints:

1 <= n == happiness.length <= 2 * 105
1 <= happiness[i] <= 108
1 <= k <= n
'''


class Solution:
    def maximumHappinessSum(self, happiness, k):
        # Sort the happiness array in ascending order
        happiness.sort()
        print(f"Sorted happiness: {happiness}")

        # Initialize the left pointer, the right pointer, and the happiness sum
        left_pointer, right_pointer = 0, len(happiness) - 1
        happiness_sum = 0

        while left_pointer < k:
            # Add the maximum of 0 and the difference between the value at the right pointer and the left pointer to the happiness sum
            happiness_sum += max(0, happiness[right_pointer] - left_pointer)
            print(f"happiness_sum: {happiness_sum}")

            # Move the left pointer one step forward and the right pointer one step backward
            left_pointer += 1
            right_pointer -= 1
            print(f"left_pointer: {
                  left_pointer}, right_pointer: {right_pointer}")

        # All k children have been selected, return the happiness sum
        return happiness_sum


sol = Solution()

print(sol.maximumHappinessSum([1, 2, 3], 2))  # 4
print(sol.maximumHappinessSum([1, 1, 1, 1], 2))  # 1
print(sol.maximumHappinessSum([2, 3, 4, 5], 1))  # 5
