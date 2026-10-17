class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d_sum=lambda x:sum(map(int,str(x)))
        r={x:k for k,x in enumerate(sorted(nums,key=lambda x:(d_sum(x),x)))}
        h=[r[x] for x in nums]
        swap=0
        for i in range(len(h)):
            while h[i]!=i:
                j=h[i]
                h[i],h[j]=h[j],h[i]
                swap+=1
        return swap