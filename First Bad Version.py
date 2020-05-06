# PROBLEM STATEMENT:

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


class Solution(object):
    def firstBadVersion(self, n):      
        if isBadVersion(1) == True :
            return 1
        if isBadVersion(n) == True and isBadVersion(n-1) == False :
            return n
        if isBadVersion(n-1) == True and isBadVersion(n-2) == False :
            return n-1
        res = self.BinSrch(0,(n-1))
        return res
    
        
    def BinSrch(self,l,r):
        mid = (l + r ) // 2
        if r>=l :
            if isBadVersion(mid+1) == True and  isBadVersion(mid ) == False :
                return (mid+1)
            if  isBadVersion(mid+1) == False :
                return self.BinSrch(mid,r)
            if  isBadVersion(mid+1) == True :
                return self.BinSrch(l, mid )
            else:
                return (mid+1)
            

# Example :

# Given n = 5, and version = 4 is the first bad version.

# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true

# Then 4 is the first bad version. 