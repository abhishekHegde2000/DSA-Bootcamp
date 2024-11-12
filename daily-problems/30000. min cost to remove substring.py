'''

https://codeforces.com/blog/entry/100661

Question 2:
Alice has a string S with length N and Bob has a string C with length M. Bob gave Alice an array of integers A of size N representing the cost of deleting each letter in strings S. Find the minimum cost T to delete a number of characters(possibly zero) from S so that C doesn't appear as a sub sequence of S.

Notes: Ai is the cost to delete Si, where 1<=i<=N.

Input format first line: N denoting the no. of elements in A.
second line: M denoting the length of C.
third line: string S, denoting the Alice's string.
fourth line: string C, denoting the Bob's string.
fifth line: contains integers describing A[i].

Sample Input:

5
3
hallo
llo
1 2 3 4 5

output: 5
explanation: if we delete the third character 'l' in string S, we wouldn't have any sub sequence equal to 'llo' in string S, achieving the minimum cost.

sample input: 8
8
muhammad
muhammad
1 2 3 4 5 6 7 8

sample output: 1 explanation: it's enough to delete the first character and this achieves the minimum cost.

sample input: 15
4
hallohallohallo
allo
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

output: 21
explanation: we have four sub sequences equal to 'allo' in string S. If we delete characters numbers 2,7 and 12 in string S, we wouldn't have any sub sequences equal to 'allo' in string S, achieving the minimum cost.

Thanks in advance!!!
'''


def helper(str, test, n, m, cost, dp):
    if m == 0:
        # If test is empty, cost is infinity (impossible case)
        return float('inf')
    if n == 0:
        return 0  # If str is empty, no cost is needed

    if (n, m) in dp:
        return dp[(n, m)]

    if str[n - 1] == test[m - 1]:
        # Delete character str[n-1]
        delete = cost[n - 1] + helper(str, test, n - 1, m, cost, dp)
        ignore = helper(str, test, n - 1, m - 1, cost,
                        dp)  # Ignore character str[n-1]
        dp[(n, m)] = min(delete, ignore)
    else:
        # Move to next character in str
        dp[(n, m)] = helper(str, test, n - 1, m, cost, dp)

    return dp[(n, m)]


def min_cost_to_delete(S, C, A):
    n = len(S)
    m = len(C)
    dp = {}
    result = helper(S, C, n, m, A, dp)
    return result


def min_cost_to_delete(S, C, A):

    n = len(S)
    m = len(C)
    dp = [[-1] * m for _ in range(n)]

    def dfs(i, j):

        if j >= m:
            return float('inf')

        if i >= n:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if S[i] == C[j]:

            delete = A[i] + dfs(i+1, j)
            ignore = dfs(i+1, j+1)

            dp[i][j] = min(delete, ignore)

        else:

            dp[i][j] = dfs(i+1, j)

        return dp[i][j]

    return dfs(0, 0)


def min_cost_to_delete_dp(S, C, A):
    n = len(S)
    m = len(C)

    # Initialize a DP table with dimensions (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(n + 1):
        for j in range(m + 1):
            if j == 0:
                # If test is empty, cost is infinity (impossible case)
                dp[i][j] = float('inf')
            elif i == 0:
                dp[i][j] = 0  # If str is empty, no cost is needed
            else:
                if S[i - 1] == C[j - 1]:
                    delete = A[i - 1] + dp[i - 1][j]
                    ignore = dp[i - 1][j - 1]
                    dp[i][j] = min(delete, ignore)
                else:
                    dp[i][j] = dp[i - 1][j]

    # The minimum cost to delete characters in S to match C
    return dp[n][m]


print(min_cost_to_delete("hallo", "llo", [1, 2, 3, 4, 5]))  # 5
print(min_cost_to_delete("muhammad", "muhammad",
      [1, 2, 3, 4, 5, 6, 7, 8]))  # 1
print(min_cost_to_delete("hallohallohallo", "allo", [
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))  # 21


print(min_cost_to_delete_dp("hallo", "llo", [1, 2, 3, 4, 5]))  # 5
print(min_cost_to_delete_dp("muhammad", "muhammad",
      [1, 2, 3, 4, 5, 6, 7, 8]))  # 1
print(min_cost_to_delete_dp("hallohallohallo", "allo", [
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))  # 21
