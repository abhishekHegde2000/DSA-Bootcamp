def find_nth_root(nth_power: int, target_value: int) -> int:
    """
    Finds the integer Nth root of M using binary search.
    Returns the integer root if exists, else -1.
    """

    print("------------------------------------------------------------")
    print(f"[Input] N (root degree) = {nth_power}, M (target value) = {target_value}")
    print("The goal is to find an integer X such that X^N = M.")
    print("We will use Binary Search because X^N increases as X increases.")
    print("------------------------------------------------------------\n")

    step = 1  # To count debug steps

    # -------------------------------------------------------------------
    # Helper function: compare mid^N with M safely (avoids overflow)
    # -------------------------------------------------------------------
    def compare_power(base: int, exponent: int, target: int) -> int:
        nonlocal step
        print(f"[Step {step}] Checking: Does {base}^{exponent} equal {target}?")
        print("   Why? This helps us decide if 'base' is too small or too large.")
        step += 1

        current_product = 1

        for power_step in range(exponent):
            print(f"      → Multiply step {power_step + 1}: current_product = {current_product}, base = {base}")
            print("        We check for overflow BEFORE multiplying.")

            # Overflow check
            if current_product > target / base:
                print("        ⚠️ Overflow/Too Large! base^N already exceeds target.")
                return 1

            current_product *= base
            print(f"        Updated current_product = {current_product}")

        # Final comparison
        if current_product == target:
            print("      → Result: EXACT match!")
            return 0
        else:
            print(f"      → Result: current_product = {current_product}, which is LESS than target.")
            return -1

    # -------------------------------------------------------------------
    # Binary Search Setup
    # -------------------------------------------------------------------
    left = 1
    right = target_value

    print(f"[Setup] Binary Search Range = [{left}, {right}]")
    print("We repeatedly pick mid and compare mid^N with M.")
    print("------------------------------------------------------------\n")

    # -------------------------------------------------------------------
    # Binary Search Loop
    # -------------------------------------------------------------------
    while left <= right:
        mid_value = left + (right - left) // 2

        print(f"[Step {step}] Binary Search Midpoint Check")
        print(f"   mid = {mid_value} (chosen as the midpoint of {left} and {right})")
        print("   Why? mid splits our search space into two halves.")
        step += 1

        comparison_result = compare_power(mid_value, nth_power, target_value)

        if comparison_result == 0:
            print(f"[Result] Found exact Nth root: {mid_value}")
            print("Binary search stops because mid^N == M.")
            return mid_value

        elif comparison_result == -1:
            print(f" → mid^N is LESS than M. So the root must be larger.")
            print(f"   Updating left boundary: {left} → {mid_value + 1}\n")
            left = mid_value + 1

        else:  # comparison_result == 1
            print(f" → mid^N is GREATER than M. So the root must be smaller.")
            print(f"   Updating right boundary: {right} → {mid_value - 1}\n")
            right = mid_value - 1

    # -------------------------------------------------------------------
    # Conclusion
    # -------------------------------------------------------------------
    print("[Final] No integer root found. The value M is not a perfect Nth power.")
    return -1


# ------------------------------------------------------------
# Test Cases (simple print-based testing)
# ------------------------------------------------------------
print("\n================= TEST CASES =================\n")
print("Test 1: N=3, M=27 → Expect 3")
print("Output:", find_nth_root(3, 27))

print("\n----------------------------------------------\n")

print("Test 2: N=4, M=69 → Expect -1")
print("Output:", find_nth_root(4, 69))

print("\n----------------------------------------------\n")

print("Test 3: N=2, M=16 → Expect 4")
print("Output:", find_nth_root(2, 16))



def find_nth_root(N: int, M: int) -> int:
    """
    Solves for the Nth root of M using binary search.
    """

    # First, I'll create a helper function. The core of this problem is
    # calculating mid^N without using built-in power functions and,
    # critically, handling overflow.
    # This helper will return:
    #   0 if base^exp == target
    #  -1 if base^exp < target
    #   1 if base^exp > target (or if it *would* overflow)
    def compare_power(base: int, exp: int, target: int) -> int:
        # We'll calculate the power iteratively. 'ans' starts at 1.
        ans = 1

        # We loop 'exp' (or N) times.
        for _ in range(exp):
            # This is the most important check. Before I multiply ans * base,
            # I must check if the result will exceed our target 'M'.
            # A direct check 'ans * base > target' could overflow if 'ans * base'
            # itself is larger than the max integer size.
            # The safe way is to check: 'ans > target / base'.
            # Since our 'base' (which is 'mid') starts from 1, division by zero isn't a risk.
            if ans > target / base:
                # If 'ans' is already greater than 'target / base',
                # then 'ans * base' will definitely be greater than 'target'.
                # We can stop early and report that our 'base' (mid) is too high.
                return 1  # 'greater than'

            # If no overflow, we perform the multiplication.
            ans = ans * base

        # After the loop, we have the final value of base^exp (or 'mid^N').
        if ans == target:
            return 0  # 'equal'
        else:
            # Since our overflow check already handles 'greater than',
            # if 'ans' is not equal, it must be 'less than'.
            return -1 # 'less than'

    # --- Main Function Logic ---

    # Okay, the problem asks for the Nth root of M.
    # My first thought is a brute-force approach: check every number 'i'
    # from 1 to M, calculate i^N, and see if it equals M.
    # That would be roughly O(M * N) in the worst case, which is very inefficient if M is large.

    # The problem has a clear monotonic property: as 'x' increases, 'x^N' also increases.
    # This immediately tells me that Binary Search is the right tool.
    # We can search for the root in the range [1, M].

    # Let's define the boundaries for our binary search.
    low = 1
    high = M

    # Standard binary search loop. It continues as long as our search space is valid.
    while low <= high:

        # I'll calculate 'mid' using 'low + (high - low) // 2'.
        # This is a good habit as it prevents potential integer overflow
        # if 'low + high' were to exceed the maximum integer size,
        # which is less of a concern in Python but shows good practice.
        mid = low + (high - low) // 2

        # Now, I'll use my helper function to check 'mid'.
        # This tells me how mid^N compares to M.
        check_result = compare_power(mid, N, M)

        if check_result == 0:
            # Perfect match. mid^N equals M. We've found the Nth root.
            return mid

        elif check_result == -1:
            # This means mid^N was *less than* M.
            # This 'mid' is too small, so the actual root must be in the right half
            # of our search space (i.e., greater than 'mid').
            # We set 'low' to 'mid + 1' to discard the left half.
            low = mid + 1

        else: # check_result == 1
            # This means mid^N was *greater than* M (or it overflowed).
            # This 'mid' is too large, so the actual root must be in the left half
            # (i.e., smaller than 'mid').
            # We set 'high' to 'mid - 1' to discard the right half.
            high = mid - 1

    # If the 'while' loop finishes, it means 'low' has crossed 'high'
    # (low > high), and we never found a 'mid' that was a perfect
    # integer root.
    # As required, I'll return -1 to indicate no integer root was found.
    return -1

# --- Example Test Cases ---
# Let's run a few mental checks.
# N = 3, M = 27
# low = 1, high = 27 -> mid = 14. compare_power(14, 3, 27) -> 1 (greater)
# low = 1, high = 13 -> mid = 7.  compare_power(7, 3, 27) -> 1 (greater)
# low = 1, high = 6  -> mid = 3.  compare_power(3, 3, 27) -> 0 (equal)
# RETURN 3. Looks correct.

# N = 4, M = 69
# low = 1, high = 69 -> ... (will search)
# Eventually it will narrow down.
# 2^4 = 16 (low = 3)
# 3^4 = 81 (high = 2)
# low becomes 3, high becomes 2. loop terminates.
# RETURN -1. Looks correct.



def find_nth_root_floor(N: int, M: int) -> int:
    """
    Solves for the floor of the Nth root of M (i.e., the largest
    integer x such that x^N <= M) using binary search.
    """

    # The helper function 'compare_power' is identical to the previous
    # problem. It's crucial for safely checking mid^N against M
    # and handling potential overflows.
    # Returns:
    #   0 if base^exp == target
    #  -1 if base^exp < target
    #   1 if base^exp > target (or overflow)
    def compare_power(base: int, exp: int, target: int) -> int:
        ans = 1
        for _ in range(exp):
            if ans > target / base:
                return 1  # Overflow, definitely greater
            ans = ans * base

        if ans == target:
            return 0  # Equal
        else:
            return -1 # Must be less than

    # --- Main Function Logic ---

    # Okay, the problem is now to find the *floor* of the Nth root.
    # This means I'm looking for the *largest* integer 'x'
    # such that x^N is less than or equal to M.

    # My binary search range is still [1, M].
    low = 1
    high = M

    # I need a variable to store the "best" answer I've found so far.
    # 'ans' will hold the largest 'mid' that satisfies mid^N <= M.
    # I'll initialize it to 0, which is a safe default floor.
    ans = 0

    # Standard binary search loop.
    while low <= high:

        # Calculate mid, preventing overflow.
        mid = low + (high - low) // 2

        # Let's check how mid^N compares to M.
        check_result = compare_power(mid, N, M)

        if check_result == 0:
            # We found an exact match! mid^N == M.
            # This is by definition the largest integer x where x^N <= M.
            # I can stop and return this immediately.
            return mid

        elif check_result == -1:
            # This means mid^N < M.
            # This 'mid' is a *valid candidate* for our answer.
            # It's the best one I've seen so far in this branch of the search.
            # So, I'll *store it* in my 'ans' variable.
            ans = mid

            # Now, I need to check if there's an even *larger* number
            # that also works. So, I'll search the right half.
            low = mid + 1

        else: # check_result == 1
            # This means mid^N > M.
            # This 'mid' is *not* a valid answer. It's too large.
            # The correct answer must be in the left half.
            high = mid - 1

    # If the loop finishes, it means 'low' has crossed 'high' and
    # we never found an *exact* match.
    # My 'ans' variable now holds the largest 'mid' we ever found
    # that was *less than* M (since all the 'greater than' ones
    # were discarded).
    # This is my floor, my lower bound.
    return ans

# --- Example Test Cases ---
# N = 3, M = 26 (Root is ~2.96. Floor should be 2)
# low = 1, high = 26 -> mid = 13. 13^3 > 26. high = 12
# low = 1, high = 12 -> mid = 6.  6^3 > 26. high = 5
# low = 1, high = 5  -> mid = 3.  3^3 = 27 > 26. high = 2
# low = 1, high = 2  -> mid = 1.  1^3 = 1 < 26. ans = 1, low = 2
# low = 2, high = 2  -> mid = 2.  2^3 = 8 < 26. ans = 2, low = 3
# low = 3, high = 2  -> loop terminates.
# RETURN ans (which is 2). This is correct.

# N = 3, M = 27 (Root is 3. Floor should be 3)
# ...
# low = 1, high = 6  -> mid = 3. 3^3 = 27. check_result = 0.
# RETURN 3 (from inside the loop). This is also correct.


