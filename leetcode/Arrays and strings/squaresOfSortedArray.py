# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0 
        j = len(nums) - 1
        idx = len(nums) - 1
        ans = [0] * len(nums)
        
        while i <= j:
            if abs(nums[j]) >= abs(nums[i]):
                ans[idx] = nums[j] ** 2
                j -= 1
            else:
                ans[idx] = nums[i] **2
                i += 1
            idx -= 1
      
        return ans
                