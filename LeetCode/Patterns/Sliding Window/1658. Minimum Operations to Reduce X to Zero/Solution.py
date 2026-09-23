class Solution(object):
    def minOperations(self, nums, x):
        a=sum(nums)-x
        if a<0:
            return -1
        best=-1
        s=0
        i=0
        for j,num in enumerate(nums):
            s+=num
            while s>a:
                s-=nums[i]
                i+=1
            if s==a:
                best=max(best,j-i+1)
        return -1 if best<0 else len(nums)-best