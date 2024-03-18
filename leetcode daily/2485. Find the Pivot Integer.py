'''
2485. Find the Pivot Integer

Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

 

Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.
Example 3:

Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.
 

Constraints:

1 <= n <= 1000

'''


class Solution:
    def pivotInteger(self, n: int) -> int:

        def findSum(start, end):
            s = sum(range(start, end+1))
            print(f"Sum of elements between {
                  start} and {end} inclusively: {s}")
            return s

        nums = list(range(1, n+1))
        print(f"List of numbers: {nums}")

        l, r = 0, n-1
        while l < r:
            m = (l+r)//2
            print(f"Middle index: {m}")
            leftSum = findSum(nums[l], nums[m])
            rightSum = findSum(nums[m], nums[r])

            if leftSum == rightSum:
                return nums[m]
            elif leftSum < rightSum:
                l = m+1
            else:
                r = m-1

        return -1


sol = Solution()

print(sol.pivotInteger(8))  # 6
print(sol.pivotInteger(1))  # 1
print(sol.pivotInteger(4))  # -1
