# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        def Counter(a):
            d = {}
            for c in a:
                d[c] = d.get(c,0) + 1
            return d
        
        ans = []
        pl = len(p)
        dp  = Counter(p)
        ds  = Counter(s[:pl-1])

        for i in range(pl-1,len(s)):
            
            ds[s[i]] = ds.get(s[i],0) + 1
            
            if ds == dp:
                ans.append(i-pl+1)

            ds[s[i-pl+1]] =  ds.get(s[i-pl+1],1) - 1
            if ds[s[i-pl+1]] == 0:
                del ds[s[i-pl+1]]
                
        return ans
