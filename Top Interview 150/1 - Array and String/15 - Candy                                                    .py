'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

'''

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Get the number of children
        num_children = len(ratings)
        # Initialize candies array with 1 for each child
        candies = [1] * num_children

        # Iterate over the children from left to right
        for i in range(1, num_children):
            # If current child's rating is higher than the previous child's rating
            if ratings[i] > ratings[i - 1]:
                # Give current child one more candy than previous child
                candies[i] = candies[i - 1] + 1
            print(f"Candies after left to right pass: {candies}")

        # Iterate over the children from right to left
        for i in range(num_children - 2, -1, -1):
            # If current child's rating is higher than the next child's rating and current child's candy is less or equal to the next child's candy
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                # Give current child one more candy than next child
                candies[i] = candies[i + 1] + 1
            print(f"Candies after right to left pass: {candies}")

        # Return the sum of all candies
        return sum(candies)


sol = Solution()
print(sol.candy([1, 0, 2]))
print(sol.candy([1, 2, 2]))
