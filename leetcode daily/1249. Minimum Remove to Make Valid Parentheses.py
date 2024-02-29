'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.

'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        S = list(s)

        # i got an  open '(' add index to stack and i got closed "(" if stack has index vales, pop it
        # if there is an empty stack and i got closed '(' , convert the string to ""

        for idx, ch in enumerate(S):

            if ch == '(':
                # add the idxndex to stack
                stack.append(idx)

            elif ch == ')':
                # if stack is present means we have already faced an open para
                if stack:
                    stack.pop()  # we have successfully removed one pair
                else:
                    # we encountered a sinle first close paranthesis
                    S[idx] = ""

        # suppose there were not closed open paranthesis left, we need to make them empty
        for ind in stack:
            S[ind] = ""

        return "".join(S)


sol = Solution()

print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))  # "lee(t(c)o)de"
print(sol.minRemoveToMakeValid("a)b(c)d"))  # "ab(c)d"
print(sol.minRemoveToMakeValid("))(("))  # ""
