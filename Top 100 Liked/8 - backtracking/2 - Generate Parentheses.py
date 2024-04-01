'''
https://leetcode.com/problems/generate-parentheses/?envType=study-plan-v2&envId=top-100-liked

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        parenthesis_stack = []
        result = []

        def backtrack(open_count, close_count):

            print(f"open_count: {open_count}, close_count: {
                  close_count}, parenthesis_stack: {parenthesis_stack}")

            if (open_count == close_count == n):
                # append the possible ans to res
                result.append("".join(parenthesis_stack))
                print(f"Found a valid combination: {result[-1]}")
                return

            if open_count < n:
                # add an opening parenthesis to the stack
                parenthesis_stack.append("(")
                print(f"Added '(': {parenthesis_stack}")

                # recursively call backtrack with open_count + 1
                backtrack(open_count + 1, close_count)

                # remove the last element from the stack
                parenthesis_stack.pop()
                print(f"Removed last element after backtrack: {
                      parenthesis_stack}")

            if close_count < open_count:
                # add a closing parenthesis to the stack
                parenthesis_stack.append(")")
                print(f"Added ')': {parenthesis_stack}")

                # recursively call backtrack with close_count + 1
                backtrack(open_count, close_count + 1)

                # remove the last element from the stack
                parenthesis_stack.pop()
                print(f"Removed last element after backtrack: {
                      parenthesis_stack}")

        backtrack(0, 0)
        return result


sol = Solution()

n = 3
print(f"n: {n}")
# ["((()))","(()())","(())()","()(())","()()()"]
print(f"Output: {sol.generateParenthesis(n)}")

n = 1
print(f"n: {n}")
print(f"Output: {sol.generateParenthesis(n)}")  # ["()"]
