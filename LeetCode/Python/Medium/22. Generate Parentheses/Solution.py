class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==1:
            return ["()"]
        n-=1
        res=[]
        def dfs(o,C,s):
            if not o and not C:
                res.append(s+")")
                return
            if o>0:
                dfs(o-1,C,s+"(")
            if C>=o:
                dfs(o,C-1,s+")")
        dfs(n,n,"(")
        return res