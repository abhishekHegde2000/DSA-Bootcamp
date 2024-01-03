'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

'''

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # If no flowers need to be placed, return True
        if n == 0:
            print("No flowers need to be placed.")
            return True

        # Iterate over the flowerbed
        for i in range(len(flowerbed)):
            print(f"Checking plot {i}")

            # If the current plot is empty and the plots to the left and right are either empty or non-existent
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                # Place a flower in the current plot
                flowerbed[i] = 1
                print(f"Placed a flower in plot {i}")

                # Decrease the number of flowers that need to be placed
                n -= 1
                print(f"{n} flowers left to place")

                # If all flowers have been placed, return True
                if n == 0:
                    print("All flowers have been placed.")
                    return True

        # If not all flowers could be placed, return False
        print("Not all flowers could be placed.")
        return False


'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Add 0s to the start and end of the flowerbed to simplify edge case handling
        flowerbed = [0] + flowerbed + [0]
        
        for i in range(1, len(flowerbed) - 1):  # Skip first and last
            # If the current plot and the plots to the left and right are all empty
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                # Place a flower in the current plot
                flowerbed[i] = 1
                # Decrease the number of flowers that need to be placed
                n -= 1

        # If all flowers have been placed (or fewer were needed), return True
        return n <= 0
'''


sol = Solution()
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))
print(sol.canPlaceFlowers([0, 0, 1, 0, 0], 2))
