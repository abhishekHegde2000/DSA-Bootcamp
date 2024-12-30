'''

2466. Count Ways To Build Good Strings
Solved
Medium
Topics
Companies
Hint
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.



Example 1:

Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation:
One possible valid good string is "011".
It can be constructed as follows: "" -> "0" -> "01" -> "011".
All binary strings from "000" to "111" are good strings in this example.
Example 2:

Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".


Constraints:

1 <= low <= high <= 105
1 <= zero, one <= low

'''


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        f = [0] * (high+1)
        f[0] = 1

        for i in range(1, high+1):
            f[i] = (f[i-zero] + f[i-one]) % MOD

        res = 0
        for i in range(low, high+1):
            res += f[i]
        return res % MOD


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = {}

        def dfs(curr_len):
            # Base case: if length exceeds high, no valid strings can be formed
            if curr_len > high:
                return 0

            # If we've already calculated this length, return memoized result
            if curr_len in dp:
                return dp[curr_len]

            # Start count with 1 if current length is in valid range, else 0
            count = 1 if low <= curr_len <= high else 0

            # Try adding 'zero' zeros
            count = (count + dfs(curr_len + zero)) % MOD

            # Try adding 'one' ones
            count = (count + dfs(curr_len + one)) % MOD

            # Memoize and return
            dp[curr_len] = count
            return count

        return dfs(0)


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = {}

        def dfs(curr_len):
            # Base case: if length exceeds high, no valid strings can be formed
            if curr_len > high:
                return 0

            # If we've already calculated this length, return memoized result
            if curr_len in dp:
                return dp[curr_len]

            # Start count with 1 if current length is in valid range, else 0
            curr = 1 if low <= curr_len <= high else 0

            # Try adding 'zero' zeros
            count_zero = dfs(curr_len + zero)

            # Try adding 'one' ones
            count_one = dfs(curr_len + one)

            # Total count = current valid string (if any) + paths with zeros + paths with ones
            count = (curr + count_zero + count_one) % MOD

            # Memoize and return
            dp[curr_len] = count
            return count

        return dfs(0)


sol = Solution()


print(sol.countGoodStrings(3, 3, 1, 1))  # 8
print(sol.countGoodStrings(2, 3, 1, 2))  # 5
print(sol.countGoodStrings(2, 3, 1, 1))  # 3
