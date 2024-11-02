'''

https://www.codingninjas.com/codestudio/problems/subset-sum-equal-to-k_1550954?leftPanelTab=0

Subset sum equal to target (DP- 14)


114

0
In this article, we will solve the most asked coding interview problem: Subset sum equal to target.

In this article, we will be going to understand the pattern of dynamic programming on subsequences of an array. We will be using the problem "Subset Sum Equal to K".

First, we need to understand what a subsequence/subset is.

A subset/subsequence is a contiguous or non-contiguous part of an array, where elements appear in the same order as the original array.
For example, for the array: [2,3,1] , the subsequences will be [{2},{3},{1},{2,3},{2,1},{3,1},{2,3,1}} but {3,2} is not a subsequence because its elements are not in the same order as the original array.

Problem Link: Subset Sum Equal to K

We are given an array ‘ARR’ with N positive integers. We need to find if there is a subset in “ARR” with a sum equal to K. If there is, return true else return false.

Examples
Practice:
Solve Problem
code-studio
Disclaimer: Don’t jump directly to the solution, try it out yourself first.

Memorization Approach
Algorithm / Intuition
Why a Greedy Solution doesn’t work?
A Greedy Solution doesn’t make sense because we are not looking to optimize anything. We can rather try to generate all subsequences using recursion and whenever we get a single subsequence whose sum is equal to the given target, we can return true.

Note: Readers are highly advised to watch this video “Recursion on Subsequences” to understand how we generate subsequences using recursion.

Steps to form the recursive solution:
We will first form the recursive solution by the three points mentioned in the Dynamic Programming Introduction.

Step 1: Express the problem in terms of indexes.

The array will have an index but there is one more parameter “target”. We are given the initial problem to find whether there exists in the whole array a subsequence whose sum is equal to the target.

So, we can say that initially, we need to find(n-1, target) which means that we need to find whether there exists a subsequence in the array from index 0 to n-1, whose sum is equal to the target. Similarly, we can generalize it for any index ind as follows:



Base Cases:

If target == 0, it means that we have already found the subsequence from the previous steps, so we can return true.
If ind==0, it means we are at the first element, so we need to return arr[ind]==target. If the element is equal to the target we return true else false.


Step 2: Try out all possible choices at a given index.

We need to generate all the subsequences. We will use the pick/non-pick technique as discussed in this video “Recursion on Subsequences”.

We have two choices:

Exclude the current element in the subsequence: We first try to find a subsequence without considering the current index element. For this, we will make a recursive call to f(ind-1,target).
Include the current element in the subsequence: We will try to find a subsequence by considering the current index as element as part of subsequence. As we have included arr[ind], the updated target which we need to find in the rest if the array will be target - arr[ind]. Therefore, we will call f(ind-1,target-arr[ind]).
Note: We will consider the current element in the subsequence only when the current element is less or equal to the target.


Step 3:  Return (taken || notTaken)

As we are looking for only one subset, if any of the one among taken or not taken returns true, we can return true from our function. Therefore, we return ‘or(||)’ of both of them.

The final pseudocode after steps 1, 2, and 3:


Steps to memoize a recursive solution:

If we draw the recursion tree, we will see that there are overlapping subproblems. In order to convert a recursive solution the following steps will be taken:

Create a dp array of size [n][k+1]. The size of the input array is ‘n’, so the index will always lie between ‘0’ and ‘n-1’. The target can take any value between ‘0’ and ‘k’. Therefore we take the dp array as dp[n][k+1]
We initialize the dp array to -1.
Whenever we want to find the answer of particular parameters (say f(ind,target)), we first check whether the answer is already calculated using the dp array(i.e dp[ind][target]!= -1 ). If yes, simply return the value from the dp array.
If not, then we are finding the answer for the given value for the first time, we will use the recursive relation as usual but before returning from the function, we will set dp[ind][target] to the solution we get.
Code
Complexity Analysis

Time Complexity: O(N*K)

Reason: There are N*K states therefore at max ‘N*K’ new problems will be solved.

Space Complexity: O(N*K) + O(N)

Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*K)).



Problem statement
You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

For Example :
If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 5
1 <= N <= 10^3
0 <= ARR[i] <= 10^9
0 <= K <= 10^3

Time Limit: 1 sec
Sample Input 1:
2
4 5
4 3 2 1
5 4
2 5 1 6 7
Sample Output 1:
true
false
Explanation For Sample Input 1:
In example 1, ‘ARR’ is {4,3,2,1} and ‘K’ = 5. There exist 2 subsets with sum = 5. These are {4,1} and {3,2}. Hence, return true.
In example 2, ‘ARR’ is {2,5,1,6,7} and ‘K’ = 4. There are no subsets with sum = 4. Hence, return false.
Sample Input 2:
2
4 4
6 1 2 1
5 6
1 7 2 9 10
Sample Output 2:
true
false
Explanation For Sample Input 2:
In example 1, ‘ARR’ is {6,1,2,1} and ‘K’ = 4. There exist 1 subset with sum = 4. That is {1,2,1}. Hence, return true.
In example 2, ‘ARR’ is {1,7,2,9,10} and ‘K’ = 6. There are no subsets with sum = 6. Hence, return false.


Hints:
1. Can you find every possible subset of ‘ARR’ and check if its sum is equal to ‘K’?
2. Can you use dynamic programming and use the previously calculated result to calculate the new result?
3. Try to use a recursive approach followed by memoization by including both index and sum we can form.
'''

from os import *
from sys import *
from collections import *
from math import *


def subsetSumToK(n, k, arr):
    dp = [[-1] * (k + 1) for _ in range(n)]

    def dfs(i, target):
        if target < 0:
            return False
        if target == 0:
            return True
        if i >= n:
            return False

        if dp[i][target] != -1:
            return dp[i][target]

        pick = dfs(i + 1, target - arr[i])
        leave = dfs(i + 1, target)

        dp[i][target] = pick or leave

        return dp[i][target]

    return dfs(0, k)


def print_subsets_with_sum_k(n, k, arr):
    dp = [[-1] * (k + 1) for _ in range(n)]
    res = []

    def dfs(i, target, path):
        if target < 0:
            return
        if target == 0:
            print(path)
            res.append(path.copy())
            return
        if i >= n:
            return

        if dp[i][target] != -1:
            return

        dfs(i + 1, target - arr[i], path + [arr[i]])
        dfs(i + 1, target, path)

        dp[i][target] = 1

    dfs(0, k, [])

    print(res)


def subsetSumToK_dp(n, k, arr):

    dp = [[False] * (k + 1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = True

    for i in range(n):
        for j in range(1, k + 1):
            if i == 0:
                dp[i][j] = arr[i] == j
            else:
                if arr[i] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i]]

    return dp[n - 1][k]


# Example usage:
n = 5
k = 9
arr = [3, 34, 4, 12, 5]
print_subsets_with_sum_k(n, k, arr)

print(subsetSumToK(4, 5, [4, 3, 2, 1]))  # True
print(subsetSumToK(5, 4, [2, 5, 1, 6, 7]))  # False
print(subsetSumToK(4, 4, [6, 1, 2, 1]))  # True
print(subsetSumToK(5, 6, [1, 7, 2, 9, 10]))  # False

print_subsets_with_sum_k(4, 5, [4, 3, 2, 1])
print_subsets_with_sum_k(5, 4, [2, 5, 1, 6, 7])
print_subsets_with_sum_k(4, 4, [6, 1, 2, 1])
print_subsets_with_sum_k(5, 6, [1, 7, 2, 9, 10])

print(subsetSumToK_dp(4, 5, [4, 3, 2, 1]))  # True
print(subsetSumToK_dp(5, 4, [2, 5, 1, 6, 7]))  # False
print(subsetSumToK_dp(4, 4, [6, 1, 2, 1]))  # True
print(subsetSumToK_dp(5, 6, [1, 7, 2, 9, 10]))  # False
