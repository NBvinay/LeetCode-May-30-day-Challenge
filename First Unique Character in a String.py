# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

class Solution(object):
    def firstUniqChar(self, s):
        d= {}
        for l in s:
            d[l] = d.get(l,0)+1

        for i,l in enumerate(s):
            if d[l] == 1:
                return (i)
        return -1
        

        