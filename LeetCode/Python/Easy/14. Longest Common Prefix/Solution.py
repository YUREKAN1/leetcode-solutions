class Solution(object):
    def longestCommonPrefix(self, strs):
        s=""
        for i in range(min(len(x) for x in strs)):
            f=strs[0][i]
            for j in range(0,len(strs)):
                if strs[j][i]!=f:
                    return s
            s+=f    
        return s


        
        