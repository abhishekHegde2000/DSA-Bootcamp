class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the elements and their indices
        num_to_index = {}
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            # If the complement exists in the dictionary, return its index along with the current index
            if complement in num_to_index:
                return [num_to_index[complement], i]
            # Otherwise, add the current element to the dictionary
            num_to_index[num] = i


sol = Solution()

print(sol.twoSum())
