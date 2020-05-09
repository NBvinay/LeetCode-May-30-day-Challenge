# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 14
# Output: false

class Solution(object):
    def isPerfectSquare(self, num):   
        def binSerach(num,l,r):
            if r>=l :
                m = (l+r)//2
                m2 = m*m
                if num == m2:
                    return True
                if m2 > num:
                    return binSerach(num,l,m-1)
                if m2 < num :
                    return binSerach(num, m+1, r)
            return False
        if num == 1 :
            return True
        return binSerach(num,0,num)
        
        

            
        