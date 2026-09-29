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
        
        def dfs(row,col,b):
            b+=1 if grid[row][col]=="(" else -1
            r=(m-1-row)+(n-1-col)

            if b<0 or b>r:
                return False
            if row==m-1 and col==n-1:
                return b==0
            return ((row+1<m and dfs(row+1,col,b)) or (col+1<n and dfs(row,col+1,b)))
        return dfs(0,0,0)        