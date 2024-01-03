'''
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1

'''
from typing import List


from typing import List


class Solution:
    '''
    def hIndexBruteForce(self, citations: List[int]) -> int:
        # Sort the citations in ascending order
        citations.sort()
        print(f"Sorted citations: {citations}")

        # Get the number of citations
        num_citations = len(citations)
        print(f"Number of citations: {num_citations}")

        # Initialize the maximum H-index to 0
        max_h_index = 0

        # Traverse the list of citations
        for i in range(num_citations):
            print(f"Checking citation {i} with value {citations[i]}")

            # If the current citation is greater than or equal to the number of citations minus the current index
            if citations[i] >= num_citations - i:
                # Update the maximum H-index
                max_h_index = max(max_h_index, num_citations - i)
                print(f"Updated max H-index: {max_h_index}")

        # Return the maximum H-index
        return max_h_index
    '''

    def hIndex(self, citations: List[int]) -> int:
        # Sort the citations in ascending order
        citations.sort()
        print(f"Sorted citations: {citations}")

        # Get the number of citations
        num_citations = len(citations)
        print(f"Number of citations: {num_citations}")

        # Initialize the start and end pointers
        start, end = 0, num_citations - 1

        # Initialize the maximum H-index to 0
        max_h_index = 0

        # While the start pointer is less than or equal to the end pointer
        while start <= end:
            # Calculate the middle index
            mid = start + (end - start) // 2
            print(f"Middle index: {mid}")

            # If the citation at the middle index is greater than or equal to the number of citations minus the middle index
            if citations[mid] >= num_citations - mid:
                # Update the maximum H-index
                max_h_index = max(max_h_index, num_citations - mid)
                print(f"Updated max H-index: {max_h_index}")

                # Move the end pointer to the left of the middle index
                end = mid - 1
            else:
                # Move the start pointer to the right of the middle index
                start = mid + 1

        # Return the maximum H-index
        return max_h_index


# example usage
sol = Solution()
citations = [3, 0, 6, 1, 5]
print(sol.hIndex(citations))
citations = [1, 3, 1]
print(sol.hIndex(citations))
