class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m,n=len(grid),len(grid[0])
        l=m+n-1
        if(l%2==1 or grid[0][0]!="(" or grid[m-1][n-1]!=")"):
            return False
        
        dp=[0]*n
        for row in range(m):
            for col in range(n):
                r=0
                if row>0:
                    r|=dp[col]
                if col>0:
                    r|=dp[col-1]
                if row==0 and col==0:
                    r=1
                dp[col]=(r<<1 if grid[row][col]=="(" else r>>1) 
        return (dp[n-1] & 1)!=0     