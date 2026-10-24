class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        v=[-1]*(n+1)
        for i in nums:
            v[i]=i
        for j in range(len(v)):
            if v[j]==-1:
                return j
        return 0
