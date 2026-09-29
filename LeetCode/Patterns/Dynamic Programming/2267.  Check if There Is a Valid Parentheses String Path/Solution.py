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
        
               