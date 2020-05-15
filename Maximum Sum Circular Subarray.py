# Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

# Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

# Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

 

# Example 1:

# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3
# Example 2:

# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
# Example 3:

# Input: [3,-1,2,-1]
# Output: 4
# Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
# Example 4:

# Input: [3,-2,2,-3]
# Output: 3
# Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
# Example 5:

# Input: [-2,-3,-1]
# Output: -1
# Explanation: Subarray [-1] has maximum sum -1
 

# Note:

# -30000 <= A[i] <= 30000
# 1 <= A.length <= 30000



class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_so_far = min_so_far = min_ending_here = max_ending_here = A[0]
        for x in A[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)    
            min_ending_here = min(x, min_ending_here + x)
            min_so_far = min(min_so_far, min_ending_here)
        print(min_so_far,max_so_far, sum(A))
        if min_so_far == sum(A):
            return max_so_far
        else:
            return max(max_so_far,sum(A)-min_so_far)
        
        
 
        # ans = -30001
        # for i in range(len(A)):
        #     a = []
        #     a = A[i:]+A[:i]
        #     max_so_far =a[0] 
        #     curr_max = a[0] 
        #     for i in range(1,len(a)): 
        #         curr_max = a[i] if (a[i] >= curr_max + a[i]) else (curr_max + a[i])
        #         max_so_far = max_so_far if max_so_far>=curr_max else curr_max
        #     ans = max_so_far if (ans < max_so_far) else ans 
        # return anss