'''
https://leetcode.com/problems/guess-number-higher-or-lower/

374. Guess Number Higher or Lower
Solved
Easy
Topics
Companies
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1

'''

from typing import List


class Solution:
    def guessNumber(self, n: int) -> int:
        # Initialize pointers to the start and end of the range
        start = 1
        end = n

        while start <= end:
            print(f"Start: {start}, End: {end}")
            # Calculate the middle number
            middle = (start + end) // 2
            print(f"Guessing: {middle}")

            # Make a guess with the middle number
            guess_result = guess(middle)
            print(f"Guess Result: {guess_result}")

            # Determine the appropriate action based on the guess result
            if guess_result == 0:
                print("Found the number.")
                return middle
            elif guess_result < 0:
                print("Guess is too high, searching lower half.")
                end = middle - 1
            else:
                print("Guess is too low, searching upper half.")
                start = middle + 1

        # Return the guessed number
        return guess(middle)


sol = Solution()
print(sol.guessNumber(10))
print(sol.guessNumber(1))
print(sol.guessNumber(2))
