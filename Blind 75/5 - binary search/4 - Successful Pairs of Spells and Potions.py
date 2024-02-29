'''2300. Successful Pairs of Spells and Potions

You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
 '''

from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success_threshold: int) -> List[int]:
        """
        Counts the successful pairs of spells and potions for a given success threshold.
        """

        # Sort potions for efficient binary search
        sorted_potions = sorted(potions)

        # Initialize list to store successful pairs
        successful_pairs_count = []

        # Iterate through each spell
        for current_spell in spells:
            pair_count = 0

            # Perform binary search to find potions that meet the success criteria
            left_pointer = 0
            right_pointer = len(sorted_potions) - 1

            while left_pointer <= right_pointer:
                middle_index = (left_pointer + right_pointer) // 2
                current_potion_strength = sorted_potions[middle_index]

                if current_potion_strength * current_spell >= success_threshold:
                    # Potion is strong enough, count it and potentially search for weaker ones
                    # Count all potions to the right
                    pair_count = len(sorted_potions) - middle_index
                    right_pointer = middle_index - 1  # Search for even weaker potions
                else:
                    # Potion is too weak, explore stronger ones
                    left_pointer = middle_index + 1

            # Append the count of successful pairs for this spell
            successful_pairs_count.append(pair_count)

        return successful_pairs_count
