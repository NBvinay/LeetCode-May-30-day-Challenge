# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

# Example 1:

# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: [3,3,7,7,10,11,11]
# Output: 10
 

# Note: Your solution should run in O(log n) time and O(1) space.


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
        	
            mid = left + (right - left) // 2
            if mid == len(nums) - 1:
                return nums[right]
            if mid == 0:
                return nums[0]
            
            if mid % 2 == 0:
                if nums[mid-1] == nums[mid]:
                    right = mid - 1
                elif nums[mid+1] == nums[mid]:
                    left = mid + 1
                else:
                    return nums[mid]

            elif mid % 2 == 1:
                if nums[mid-1] == nums[mid]:
                    left = mid + 1
                elif nums[mid+1] == nums[mid]:
                    right = mid - 1
                else:
                    return nums[mid]
        