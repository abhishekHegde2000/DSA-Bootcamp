'''
https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

Subset Sum Problem

Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 


Example 1:

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 9
Output: 1 
Explanation: Here there exists a subset with
sum = 9, 4+3+2 = 9.
Example 2:

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 30
Output: 0 
Explanation: There is no subset with sum 30.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function isSubsetSum() which takes the array arr[], its size N and an integer sum as input parameters and returns boolean value true if there exists a subset with given sum and false otherwise.
The driver code itself prints 1, if returned value is true and prints 0 if returned value is false.
 

Expected Time Complexity: O(sum*N)
Expected Auxiliary Space: O(sum*N)
 

Constraints:
1 <= N <= 100
1<= arr[i] <= 100
1<= sum <= 104

'''


# User function Template for python3

class Solution:
    def isSubsetSum(self, N, arr, sum):

        dp = [[False] * (sum + 1) for i in range(N + 1)]

        def dfs(ind, target):

            if target == 0:
                return True

            if ind == 0:
                return False

            if dp[ind][target] != False:
                return dp[ind][target]

            if arr[ind - 1] <= target:
                dp[ind][target] = dfs(
                    ind - 1, target - arr[ind - 1]) or dfs(ind - 1, target)
                return dp[ind][target]

            dp[ind][target] = dfs(ind - 1, target)
            return dp[ind][target]

        return 1 if dfs(N, sum) else 0


sol = Solution()

print(sol.isSubsetSum(6, [3, 34, 4, 12, 5, 2], 9))  # 1
print(sol.isSubsetSum(6, [3, 34, 4, 12, 5, 2], 30))  # 0
print(sol.isSubsetSum(5, [3, 34, 4, 12, 5], 30))  # 1
