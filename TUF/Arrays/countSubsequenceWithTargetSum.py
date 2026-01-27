from typing import List

class Solution:
    def findRepeatingAndMissing(self, nums: List[int]) -> List[int]:
        """
        Solved using the XOR method to achieve O(N) time complexity and O(1) space complexity.
        """
        n = len(nums)

        # -------------------------------------------------------------------------
        # Step 1: Calculate the Combined XOR
        # -------------------------------------------------------------------------
        # I start by acknowledging that XOR is its own inverse (x ^ x = 0).
        # If I XOR all elements in the input array `nums` against the ideal range [1, n],
        # every number that appears correctly (once in nums, once in range) will cancel out.
        # The repeating number A will appear 3 times (twice in nums, once in range) -> leaving A.
        # The missing number B will appear 1 time (zero in nums, once in range) -> leaving B.
        # Therefore, the result will be A ^ B.

        combined_xor = 0

        # Conversational Logic: I'll iterate through the array and the range simultaneously.
        for i in range(n):
            combined_xor ^= nums[i]
            combined_xor ^= (i + 1)

        # DATA STATE SNAPSHOT (Dry Run)
        # Input: nums = [3, 5, 4, 1, 1], n = 5
        # -------------------------------------
        # Ideal Range: [1, 2, 3, 4, 5]
        # Actual Nums: [3, 5, 4, 1, 1]
        #
        # XOR Operation trace:
        # (3^3) cancels -> 0
        # (5^5) cancels -> 0
        # (4^4) cancels -> 0
        # (1^1) from range/array cancels -> 0
        # Remaining: 1 (from array duplicate) ^ 2 (from range missing)
        # combined_xor = 1 ^ 2 = 3 (Binary: 011)

        # -------------------------------------------------------------------------
        # Step 2: Isolate the Differentiating Bit
        # -------------------------------------------------------------------------
        # Conversational Logic: Now I have (A ^ B). Since A != B, the result must be non-zero.
        # Any set bit in `combined_xor` represents a position where A and B have different bits
        # (one has 0, the other has 1).
        # Why rightmost? It's the easiest to isolate programmatically.
        # I'll use the trick (x & -x) to isolate the rightmost set bit.

        rightmost_set_bit = combined_xor & -combined_xor

        # DATA STATE SNAPSHOT
        # combined_xor = 3 (Binary ...00011)
        # -combined_xor (Two's complement) = (Binary ...11101)
        # 3 & -3 = ...00011 & ...11101 = ...00001
        # rightmost_set_bit = 1 (Binary 001)

        # -------------------------------------------------------------------------
        # Step 3: Bucket Separation
        # -------------------------------------------------------------------------
        # Conversational Logic: I can now divide all numbers (both from the array and the range [1, n])
        # into two buckets based on whether this specific bit is set or not.
        # Bucket 1: Numbers where the bit is SET.
        # Bucket 2: Numbers where the bit is UNSET.
        #
        # Why do this?
        # Since A and B differ at this bit, one will fall into Bucket 1 and the other into Bucket 2.
        # All other non-problematic numbers will appear exactly twice (once in array, once in range)
        # and will fall into the SAME bucket, canceling each other out when XORed.

        bucket_one = 0 # Will hold the XOR result of numbers with the bit SET
        bucket_two = 0 # Will hold the XOR result of numbers with the bit UNSET

        # Helper logic inline for clarity: Process array numbers first
        for num in nums:
            if (num & rightmost_set_bit) != 0:
                bucket_one ^= num
            else:
                bucket_two ^= num

        # Helper logic inline: Process range numbers [1, n]
        for i in range(1, n + 1):
            if (i & rightmost_set_bit) != 0:
                bucket_one ^= i
            else:
                bucket_two ^= i

        # DATA STATE SNAPSHOT (Dry Run Continued)
        # rightmost_set_bit = 1
        # We classify numbers based on if (num & 1) is non-zero (i.e., is the number odd?)
        #
        # 1. Processing Array [3, 5, 4, 1, 1]:
        #    - 3 (011): Bit set -> bucket_one ^= 3
        #    - 5 (101): Bit set -> bucket_one ^= 5
        #    - 4 (100): Bit unset -> bucket_two ^= 4
        #    - 1 (001): Bit set -> bucket_one ^= 1
        #    - 1 (001): Bit set -> bucket_one ^= 1
        #
        # 2. Processing Range [1, 2, 3, 4, 5]:
        #    - 1 (001): Bit set -> bucket_one ^= 1
        #    - 2 (010): Bit unset -> bucket_two ^= 2
        #    - 3 (011): Bit set -> bucket_one ^= 3
        #    - 4 (100): Bit unset -> bucket_two ^= 4
        #    - 5 (101): Bit set -> bucket_one ^= 5
        #
        # 3. Final Cancellation:
        #    - bucket_one = (3^5^1^1) ^ (1^3^5)
        #      -> 3s cancel, 5s cancel, two 1s cancel.
        #      -> Remaining: 1
        #    - bucket_two = (4) ^ (2^4)
        #      -> 4s cancel.
        #      -> Remaining: 2
        #
        # Current State: bucket_one = 1, bucket_two = 2

        # -------------------------------------------------------------------------
        # Step 4: Identify Repeating vs Missing
        # -------------------------------------------------------------------------
        # Conversational Logic: I have the two unique numbers, 1 and 2.
        # However, I don't know which is the repeating number (A) and which is missing (B).
        # The logic didn't preserve order.
        # I need to scan the original array one last time. If I find `bucket_one` in the array,
        # then `bucket_one` is the repeating number. Otherwise, `bucket_two` is.

        repeating = 0
        missing = 0

        # Simple linear scan to check count
        count_bucket_one = 0
        for num in nums:
            if num == bucket_one:
                count_bucket_one += 1

        if count_bucket_one == 2:
            # I found bucket_one twice, so it must be the repeating number.
            repeating = bucket_one
            missing = bucket_two
        else:
            # If bucket_one is not repeating, bucket_two must be.
            repeating = bucket_two
            missing = bucket_one

        return [repeating, missing]
