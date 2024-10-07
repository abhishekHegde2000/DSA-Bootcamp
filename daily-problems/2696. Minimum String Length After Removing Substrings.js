/*
https://leetcode.com/problems/minimum-string-length-after-removing-substrings/


2696. Minimum String Length After Removing Substrings
Easy
Topics
Companies
Hint
You are given a string s consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

 

Example 1:

Input: s = "ABFCACDB"
Output: 2
Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.
Example 2:

Input: s = "ACBBD"
Output: 5
Explanation: We cannot do any operations on the string so the length remains the same.
 

Constraints:

1 <= s.length <= 100
s consists only of uppercase English letters.

*/
// # Brute force solution
function minLength(s) {
    console.log('stack');
    var stack = [];
    for (var _i = 0, s_1 = s; _i < s_1.length; _i++) {
        var char = s_1[_i];
        // Check if the current character and the top of the stack form "AB" or "CD"
        if (stack.length > 0 && ((stack[stack.length - 1] === 'A' && char === 'B') || (stack[stack.length - 1] === 'C' && char === 'D'))) {
            // Pop the stack if a match is found
            var removedChar = stack.pop();
            console.log("Removed '".concat(removedChar).concat(char, "', new stack: ").concat(stack));
        }
        else {
            // Push the current character onto the stack
            stack.push(char);
            console.log("Added '".concat(char, "', new stack: ").concat(stack));
        }
    }
    // The length of the stack is the length of the resulting string
    return stack.length;
}
;
console.log(minLength("ABFCACDB")); // 2
console.log(minLength("ACBBD")); // 5
console.log(minLength("ABAB")); // 0
