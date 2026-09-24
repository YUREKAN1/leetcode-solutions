class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            a=nums[i]
            t=0

            while a>0:
                t+=a%10
                a//=10
            if t==i:
                return i
        return -1
        