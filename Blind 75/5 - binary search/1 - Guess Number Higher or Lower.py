'''
374. Guess Number Higher or Lower

Companies
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Finds the target number using binary search and the guess() function.

        Args:
            n: The upper bound of the search range.

        Returns:
            The guessed target number.
        """

        # Initialize variables with meaningful names
        lowest_possible_guess = 1
        highest_possible_guess = n

        while lowest_possible_guess <= highest_possible_guess:
            # Calculate the middle value as the current guess
            current_guess = (lowest_possible_guess +
                             highest_possible_guess) // 2

            # Debugging print statement
            print(f"Current guess: {current_guess}")

            # Compare the current guess with the target number using the guess() function
            result = guess(current_guess)

            if result == 0:
                # Target found, return the current guess
                return current_guess
            elif result < 0:
                # Target is lower, adjust the search range
                highest_possible_guess = current_guess - 1
            else:
                # Target is higher, adjust the search range
                lowest_possible_guess = current_guess + 1

        # If the loop completes without finding a match, return the final guess
        return current_guess


sol = Solution()
print(sol.guessNumber(10))
print(sol.guessNumber(6))
