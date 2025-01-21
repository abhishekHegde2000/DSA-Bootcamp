'''

https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/





2116. Check if a Parentheses String Can Be Valid
Medium
Topics
Companies
Hint
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.



Example 1:


Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
Example 2:

Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.
Example 3:

Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0].
Changing s[0] to either '(' or ')' will not make s valid.


Constraints:

n == s.length == locked.length
1 <= n <= 105
s[i] is either '(' or ')'.
locked[i] is either '0' or '1'.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
41.1K
Submissions
116.3K
Acceptance Rate
35.4%
Topics
Companies
Hint 1
Can an odd length string ever be valid?
Hint 2
From left to right, if a locked ')' is encountered, it must be balanced with either a locked '(' or an unlocked index on its left. If neither exist, what conclusion can be drawn? If both exist, which one is more preferable to use?
Hint 3
After the above, we may have locked indices of '(' and additional unlocked indices. How can you balance out the locked '(' now? What if you cannot balance any locked '('?



'''


'''
Editorial:



Solution
Overview
We are given two strings, s and locked. The string s is a sequence of parentheses, consisting of opening brackets ( and closing brackets ). The string locked is a binary string of the same length as s, where:

If locked[i] is 1, the character at index i in s cannot be changed.

If locked[i] is 0, the character can be modified: an opening bracket ( can become a closing bracket ) and vice versa.

Our task is to determine if it’s possible to make the sequence in s balanced by modifying the characters marked as changeable (locked[i] = 0).

What does a balanced parentheses sequence mean?

A sequence of parentheses is considered balanced if:

Every opening bracket ( has a corresponding closing bracket ).
The brackets are properly nested. For example, (()) is balanced, but ())( is not.
To gain familiarity with similar parentheses-based problems, you may first solve an easier version: 20. Valid Parentheses.

Approach 1: Stack
Intuition
To get a good intuition to this problem, we need to ensure that at any point while iterating through s, the number of closing brackets ) should not exceed the number of opening brackets ( and by the end of the string, the total number of opening and closing brackets must be equal.

Observe that the locked characters (locked[i] = 1) cannot be modified, so they must remain fixed. However, we have the flexibility to assign the unlocked characters (locked[i] = 0) as either opening or closing brackets, depending on what is needed to maintain balance.

The main challenge is that if at any point the number of closing brackets exceeds the number of opening brackets and there are no unlocked characters available to "fix" the imbalance, it’s impossible to balance the string, and we return false.

And to address this, we need a way to keep track of all previously encountered unlocked characters so we can use them later if needed. Thus a stack is a suitable data structure for this, because it follows the Last In, First Out (LIFO) principle, which works well for keeping track of unmatched brackets.

To implement this, we iterate through the string, whenever we encounter an unlocked character (locked[i] = 0), we push its index onto the stack.

If we encounter a closing bracket ) and find that the number of closing brackets exceeds the number of opening brackets at that point, we can "fix" the imbalance by popping an index from the stack and treating that unlocked character as an opening bracket (.

If at any point we need an unlocked character to balance the string but the stack is empty (i.e., there are no more unlocked characters left), it means balancing the string is impossible, and we return false.

After processing all the characters in the string:

If the stack still contains indices of unused unlocked characters, we can pair them up to form balanced brackets, such as ()()().
As long as the number of opening and closing brackets is equal by the end, the string is balanced, and we return true.
Algorithm
If the length of the string s is odd, return false because an odd-length string cannot have balanced parentheses.

Use a stack openBrackets to keep track of the indices of open parentheses '(' in the locked positions and a stack unlocked to keep track of the indices of positions where parentheses can be changed (locked[i] == '0').

For each character in the string s, check:

If the position is unlocked (i.e., locked[i] == '0'), add its index to the unlocked stack.
If the character is an open parenthesis '(', add its index to the openBrackets stack.
If the character is a close parenthesis ')':
If there is a matching open parenthesis (i.e., the openBrackets stack is not empty), pop the stack.
If no open parenthesis is available, try to use an unlocked position and pop the unlocked stack to match with it.
If neither an open parenthesis nor an unlocked position is available to match, return false.
After processing all characters, check if there are any unmatched open parentheses remaining in the openBrackets stack.

If there are unmatched open parentheses, try to match them with the available unlocked positions and pop the stacks.
If any open parentheses remain unmatched, return false. Otherwise, return true.
Implementation

Complexity Analysis
Let n be the size of the string s.

Time Complexity: O(n)

The algorithm performs two passes over the string s:

In the first pass, it iterates through the string to process open brackets and unlocked positions, which takes O(n) time.
In the second pass, it matches the remaining open brackets with unlocked characters, which also takes O(n) time.
Therefore, the total time complexity is O(n).

Space Complexity: O(n)

The algorithm uses two stacks, openBrackets and unlocked, to store indices of open brackets and unlocked characters, respectively. In the worst case, each list can store up to n elements.

Therefore, the total space complexity is O(n).

Approach 2: Constant Space
Intuition
In the previous approach, we used a stack to store the unlocked characters and open brackets in the order they appear in the string. However, do we actually need a stack, or is a simple count of the unlocked characters and open brackets sufficient?

The stack indices are required when matching the remaining opening brackets with the unlocked characters, as shown in the code snippet below:

// Match remaining open brackets with unlocked characters
while (!openBrackets.empty() && !unlocked.empty() &&
       openBrackets.top() < unlocked.top()) {
    openBrackets.pop();
    unlocked.pop();
}
To address this, we could explore a trick to match the brackets using only the counts of the unpaired opening brackets and unlocked characters.

Since we want to balance the remaining opening brackets, note that the unlocked characters towards the end of the string can be converted into closing brackets to pair them up. This allows us to iterate from the end of the string s while maintaining a balance variable to check whether the parentheses are balanced.

We use the integer counters openBrackets and unlocked from the previous steps:

If we encounter an unlocked character, we can treat it as a closing bracket.
If the balance variable indicates that the string is unbalanced at any point, we return false.
Finally, if all the openBrackets are balanced by the end of the iteration, we can return true. Otherwise, we return false.

Algorithm
Initialize length as the size of the string s.

Check if the length is odd:

If length % 2 == 1, return false.
Initialize variables:

openBrackets to count the unmatched opening brackets.
unlocked to count the wildcard positions.
Perform a forward pass to process the string:

Iterate through s from left to right.
For each character:
If locked[i] == '0', increment unlocked.
If s[i] == '(', increment openBrackets.
If s[i] == ')':
If openBrackets > 0, decrement openBrackets.
Else if unlocked > 0, decrement unlocked.
Else, return false.
Perform a reverse pass to match remaining open brackets:

Initialize balance to track excess unmatched opening brackets.
Iterate through s from right to left.
For each character:
If locked[i] == '0', decrement balance and unlocked.
If s[i] == '(', increment balance and decrement openBrackets.
If s[i] == ')', decrement balance.
If balance > 0, return false.
If unlocked == 0 and openBrackets == 0, break out of the loop.
After the reverse pass:

If openBrackets > 0, return false.
Return true if no unmatched brackets remain.

Implementation

Complexity Analysis
Let n be the size of the string s.

Time Complexity: O(n)

The algorithm performs two passes over the string s:

In the first pass, it iterates through the string to process open brackets and unlocked positions, which takes O(n) time.
In the second pass, it iterates from the end of the string to balance the remaining open brackets with unlocked characters, which also takes O(n) time.
Therefore, the total time complexity is O(n).

Space Complexity: O(1)

The algorithm uses a constant amount of space for variables like openBrackets, unlocked, and balance. It does not use any additional data structures such as stacks or lists.

Therefore, the total space complexity is O(1).generateParenthesis
'''


class Solution:
    def canBeValid(self, s, locked):
        length = len(s)

        # If length of string is odd, return false.
        if length % 2 == 1:
            return False

        open_brackets = []
        unlocked = []

        # Iterate through the string to handle '(' and ')'
        for i in range(length):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                open_brackets.append(i)
            elif s[i] == ")":
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        # Match remaining open brackets and the unlocked characters
        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()

        if open_brackets:
            return False

        return True


sol = Solution()


print(sol.canBeValid("))()))", "010100"))  # True
print(sol.canBeValid("()()", "0000"))  # True
print(sol.canBeValid(")", "0"))  # False
