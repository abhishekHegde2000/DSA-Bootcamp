'''

https://leetcode.com/discuss/study-guide/1405817/backtracking-algorithm-problems-to-practice

https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-100-liked

17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.




Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

'''

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Initialize an empty list to store the results
        combinations = []
        print(f"Initialized combinations: {combinations}")

        # Define a dictionary to map digits to characters
        digit_to_chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        print(f"Digit to character mapping: {digit_to_chars}")

        # Define the backtracking function
        def backtrack(index, current_combination):
            print(f"\nBacktracking function called with index: {
                  index}, current_combination: {current_combination}")

            # Check if the current_combination is a valid combination
            if len(current_combination) == len(digits):
                print(f"Current combination '{
                      current_combination}' is a valid combination")
                # Add the current_combination to the combinations
                combinations.append(current_combination)
                print(f"Added '{current_combination}' to combinations. Current combinations: {
                      combinations}")
                return

            # Iterate over each character in the digit's mapping
            for char in digit_to_chars[digits[index]]:
                print(f"Processing character '{
                      char}' for digit '{digits[index]}'")
                # Recursively call the backtrack function with the next digit and the current_combination + the new character
                backtrack(index + 1, current_combination + char)
                print(f"Backtracked with index: {
                      index + 1}, current_combination: {current_combination + char}")

        # Check if the input is not empty
        if digits:
            print(f"\nInput is not empty. Starting backtracking.")
            # Start backtracking from the first digit
            backtrack(0, "")
            print(f"Backtracking started with index: 0, current_combination: ''")

        # Return the result
        print(f"\nFinal result: {combinations}")
        return combinations


sol = Solution()
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(sol.letterCombinations("23"))
print(sol.letterCombinations(""))  # []
print(sol.letterCombinations("2"))  # ["a","b","c"]
