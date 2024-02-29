'''
https://leetcode.com/problems/longest-valid-parentheses/

32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring


Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # we have an empty stack
        stack = [-1]

        mx = 0

        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            else:

                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mx = max(mx, i - stack[-1])
        return mx


sol = Solution()
print(sol.longestValidParentheses("(()"))  # 2
print(sol.longestValidParentheses(")()())"))  # 4
print(sol.longestValidParentheses(""))  # 0
