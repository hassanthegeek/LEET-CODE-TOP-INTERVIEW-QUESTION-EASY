from typing import List

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""





class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        i = 0
        zero_counts = 0
        size = len(nums)
        while i < size:
          if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
          else:
            zero_counts  += 1

          i += 1

        i = len(nums) - zero_counts
        while i < size:
          nums[i] = 0
          i += 1