# Interviewer: "You mentioned not using `pow`. That's a great point,
# especially given the risk of overflow or precision issues with
# floating-point numbers if we weren't careful.
#
# Okay, so if I can't use `pow`, I need to compute `mid^n` myself.
# The immediate challenge isn't just *computing* it, it's that
# `mid^n` can become *astronomically* large, far exceeding M.
#
# So, I'll create a helper function. Its job isn't to *return* `mid^n`.
# Its job is to *check* if `mid^n` is equal to, greater than,
# or less than M, and to *stop* the moment it knows.
# This prevents us from calculating, say, 1000^100.
#
# I'll have this function return:
#  0 if mid^n == m (exact match)
#  1 if mid^n > m (too big)
# -1 if mid^n < m (too small)
#
# This helper function is the first of the two functions you mentioned."

def check_power_against_target(base, exp, target):
    """
    Calculates `base^exp` and compares it to `target`.

    Returns:
     0 if base^exp == target
     1 if base^exp > target
    -1 if base^exp < target

    This function is designed to prevent overflow by checking
    at each multiplication step.
    """

    # "Let's initialize our running result to 1."
    ans = 1

    # "I'll loop 'exp' (which is N) times."
    # "A full binary exponentiation (O(log N)) is fast, but
    # actually a simple O(N) loop is *safer* here, because it
    # lets me check for overflow *at every single multiplication*."
    for _ in range(exp):

        # --- Critical Overflow Check ---
        # "This is the most important part of this helper."
        # "I'm about to do `ans = ans * base`."
        # "If `ans` is already, say, 100, `base` is 10,
        # and our `target` (M) is 900, then `ans * base` (1000)
        # will be > 900.
        #
        # "The standard, safe way to check this without
        # *actually* overflowing is to use division:
        # `ans * base > target` is the same as `ans > target / base`."
        #
        # "I must be careful with integer division. If base is 0...
        # no, `base` (which is `mid`) will be >= 1 in my search.
        # So `base` is at least 1."

        # "If `base` is 1, `target / base` is fine.
        # If `target` (M) is 0, this check won't run as
        # I'll handle M=0 in the main function."

        if base == 0:
            # "This should never happen if mid starts at 1,
            # but as a robust check:"
            return -1 # 0^N is 0, which is < M (assuming M > 0)

        # "Here's the check:"
        if ans > target / base:
            # "We've crossed the 'target' threshold."
            # "No need to continue looping. `base^exp` is
            # definitely greater than `target`."
            return 1  # 1 signifies 'too big'

        # "We're safe. Let's do the multiplication."
        ans = ans * base

    # "The loop finished *without* ever going over the target."
    # "Now I just need to check the final result."
    if ans == target:
        return 0  # 0 signifies 'exact match'
    else:
        # "Since we never went *over* (returned 1),
        # 'ans' must be less than 'target'."
        return -1 # -1 signifies 'too small'


# --- Main Function ---

# "Now, for the second function, the main `find_nth_root`.
# This will look almost identical to the `pow` solution,
# but instead of `val = pow(mid, n)`, I'll call my
# new helper: `status = check_power_against_target(mid, n, m)`."

def find_nth_root(n, m):
    # "Okay, starting the main function."

    # --- Edge Cases ---

    # "First, if M is 0, the Nth root is 0."
    if m == 0:
        return 0

    # "If M is 1, the Nth root is 1."
    if m == 1:
        # "This would be found by the binary search
        # [1, 1] -> mid=1, but it's clean to handle."
        return 1

    # "If N is 1, the 1st root of M is just M."
    if n == 1:
        return m

    # "If N is 0... X^0 = 1. So if M=1, any X works (we
    # returned 1 above). If M != 1, no solution.
    # The problem implies N >= 1, so I'll assume that.
    # But this is a good clarifying question for an interviewer."

    # --- Binary Search Setup ---

    # "My search space for the root X is from 1 to M."
    # "1 is the smallest possible integer root."
    # "M is a safe upper bound (e.g., for N=1, root=M)."
    low = 1
    high = m

    # "Standard binary search loop."
    while low <= high:

        # "Get the midpoint, using the overflow-safe method."
        mid = low + (high - low) // 2

        # "Here's the change. I'm not calculating the power.
        # I'm *checking* it against M."
        status = check_power_against_target(mid, n, m)

        # --- Logic Justification ---

        if status == 0:
            # "Got it! `mid^n` is exactly `m`."
            return mid

        elif status == 1:
            # "This means `mid^n` was *greater* than `m`.
            # 'mid' is too big. The answer must be
            # in the left half."
            high = mid - 1

        else: # status == -1
            # "This means `mid^n` was *less* than `m`.
            # 'mid' is too small. The answer must be
            # in the right half."
            low = mid + 1

    # "If the loop finishes, 'low' crossed 'high'
    # and we never found an exact match (status 0).
    # This means no integer root exists."
    return -1

# --- My internal test cases ---
# Test 1: n=3, m=27
# low=1, high=27 -> mid=14. check(14, 3, 27) -> 14 > 27/14 (false). 14*14=196.
# 196 > 27/14 (true). Returns 1 (too big). high = 13.
# low=1, high=13 -> mid=7. check(7, 3, 27) -> ... returns 1 (too big). high = 6.
# low=1, high=6  -> mid=3. check(3, 3, 27) -> ans=1 -> ans=3 -> ans=9 -> ans=27.
# Loop ends. ans == target. Returns 0.
# Main function gets 0. Returns mid (3). CORRECT.

# Test 2: n=2, m=10 (non-integer)
# low=1, high=10 -> mid=5. check(5, 2, 10) -> ans=1 -> 1 > 10/5 (false). ans=5.
# 5 > 10/5 (true). Returns 1 (too big). high = 4.
# low=1, high=4  -> mid=2. check(2, 2, 10) -> ans=1 -> ans=2 -> ans=4.
# Loop ends. ans < target. Returns -1 (too small). low = 3.
# low=3, high=4  -> mid=3. check(3, 2, 10) -> ans=1 -> ans=3 -> ans=9.
# Loop ends. ans < target. Returns -1 (too small). low = 4.
# low=4, high=4  -> mid=4. check(4, 2, 10) -> ans=1 -> ans=4.
# 4 > 10/4 (true). Returns 1 (too big). high = 3.
# low=4, high=3. Loop terminates.
# Main function returns -1. CORRECT.
# The logic is sound.
