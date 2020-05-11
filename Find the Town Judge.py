# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.


# Example 1:

# Input: N = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
# Example 4:

# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1
# Example 5:

# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3
 

# Note:

# 1 <= N <= 1000
# trust.length <= 10000
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N



class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        # if len(trust) == 0:
        #     return 1
        # judge = {}     
        # for item in trust:
        #     temp = judge.get(item[1],[])
        #     temp.append(item[0])
        #     judge[item[1]] = temp      
        # does_judge_trust = 0
        # for key in judge.keys():
        #     if len(judge[key]) + 1 == N:
        #         for trust_list in judge.values():
        #             if key in trust_list:
        #                 does_judge_trust = 1
        #                 break
        #         if does_judge_trust == 0:
        #             return key
        # return -1
        
        
        # below is a better approach for the same problem : 
        
        
        if len(trust) == 0:
            return 1
        judge = [] 
        n_list = [ i for i in range(1,N+1) ]  
        for item in trust:
            judge.append( item[0] )
        judge = list(set(n_list) - set(judge))       
        if len(judge) == 0:
            return -1       
        d= {}      
        for (x,y) in trust:
            d[y] = d.get(y,0) + 1
        for key in d.keys():
            if d[key] == N-1 and  key in judge:
                return key
        return -1
