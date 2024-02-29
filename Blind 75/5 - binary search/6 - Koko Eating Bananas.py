'''
https://leetcode.com/problems/koko-eating-bananas/

875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, 
the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile.


If the pile has less than k bananas, 
she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 '''


from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        print(f"piles = {piles} and h = {h}")
        left, right = 1, max(piles)
        res = right

        while left <= right:
            print(f"left = {left} , right = {right}")
            k = left + (right - left) // 2
            print(f"k(middle) = {k}")
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                res = min(res, k)

                right = k - 1
            else:
                left = k+1
        return res


sol = Solution()

# Test Case 1: Basic Test
piles1 = [3, 6, 7, 11]
h1 = 8
print(sol.minEatingSpeed(piles1, h1))  # Expected output: 4

# Test Case 2: Edge Case with minimum values
piles2 = [1, 2, 3]
h2 = 1
print(sol.minEatingSpeed(piles2, h2))  # Expected output: 3

# Test Case 3: Larger piles with more available hours
piles3 = [30, 11, 23, 4, 20]
h3 = 6
print(sol.minEatingSpeed(piles3, h3))  # Expected output: 23

# Test Case 4: All piles can be eaten within the given hours
piles4 = [30, 11, 23, 4, 20]
h4 = 50
print(sol.minEatingSpeed(piles4, h4))  # Expected output: 4

# Test Case 5: Random values
piles5 = [8, 16, 30, 12, 25, 20]
h5 = 30
print(sol.minEatingSpeed(piles5, h5))  # Expected output: 12
