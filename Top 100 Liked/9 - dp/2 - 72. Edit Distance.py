'''

https://leetcode.com/problems/edit-distance/

72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''

# Space optimized approach bottom up


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        cache = [[float('inf') for _ in range(len(word2)+1)]
                 for _ in range(len(word1)+1)]

        for j in range(len(word1)+1):
            cache[j][len(word2)] = len(word1) - j

        for i in range(len(word2)+1):
            cache[len(word1)][i] = len(word2) - i

        for r in range(len(word1) - 1, -1, -1):
            for c in range(len(word2) - 1, -1, -1):

                if word1[r] == word2[c]:
                    cache[r][c] = cache[r+1][c+1]
                else:
                    cache[r][c] = 1 + \
                        min(cache[r+1][c], cache[r][c+1], cache[r+1][c+1])
        return cache[0][0]


# spce optimized top to bottom approach

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Initialize a 2D array `dp`
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        print(f"Initial dp: {dp}")

        # Fill the first row and the first column of `dp`
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        print(f"Dp after filling first row and column: {dp}")

        # Iterate over `dp` from left to right and from top to bottom
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                # If the current characters in `word1` and `word2` are the same
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # If the current characters in `word1` and `word2` are different
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                print(f"Dp after processing cell ({i}, {j}): {dp}")

        # Return the value in the bottom-right cell of `dp`
        return dp[-1][-1]


# Memoization approach

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Define a helper function `editDistanceUtil`
        def editDistanceUtil(i: int, j: int) -> int:
            # If `i` is less than 0, return `j + 1`
            if i < 0:
                return j + 1
            # If `j` is less than 0, return `i + 1`
            if j < 0:
                return i + 1

            # If the value in `dp[i][j]` is not -1, return it
            if dp[i][j] != -1:
                return dp[i][j]

            # If the current characters in `word1` and `word2` are the same
            if word1[i] == word2[j]:
                dp[i][j] = editDistanceUtil(i - 1, j - 1)
            # If the current characters in `word1` and `word2` are different
            else:
                dp[i][j] = 1 + min(editDistanceUtil(i - 1, j - 1),
                                   editDistanceUtil(i - 1, j), editDistanceUtil(i, j - 1))
            print(f"Dp after processing cell ({i}, {j}): {dp}")

            # Return the value in `dp[i][j]`
            return dp[i][j]

        # Initialize a 2D array `dp`
        dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]
        print(f"Initial dp: {dp}")

        # Call the `editDistanceUtil` function with `len(word1) - 1` and `len(word2) - 1` as input
        return editDistanceUtil(len(word1) - 1, len(word2) - 1)


sol = Solution()
print(sol.minDistance("horse", "ros"))  # 3
print(sol.minDistance("intention", "execution"))  # 5
print(sol.minDistance("", ""))  # 0
