class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b=prices[0]
        p=0
        for i in prices[1:]:
            if b>i:
                b=i
            p=max(p,i-b)
        return p