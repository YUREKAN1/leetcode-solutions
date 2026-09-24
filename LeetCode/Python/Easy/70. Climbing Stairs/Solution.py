class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 1
        p,c=1,1
        for i in range(2,n+1):
            temp=c
            c=p