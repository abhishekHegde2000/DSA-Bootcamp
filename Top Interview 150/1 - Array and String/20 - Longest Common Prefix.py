'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

from typing import List

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) < 2:
            return strs[0]

        strs.sort()
        i = 0

        ans = ''

        while i < len(strs[0]) and i < len(strs[-1]):
            # print(f"i is {i}")
            # print(f"ans is {ans}")
            # print(f"strs[0][i] is {strs[0][i]}")
            # print(f"strs[-1][i] is {strs[-1][i]}")
            if strs[0][i] == strs[-1][i]:
                ans += strs[0][i]
                i += 1
            else:
                break

        return ans


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
