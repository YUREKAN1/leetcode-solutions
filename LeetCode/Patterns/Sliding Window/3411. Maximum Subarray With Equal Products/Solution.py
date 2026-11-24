class Solution:
    def maxLength(self, nums: List[int]) -> int:
        b,l,p=2,0,1
        for r,x in enumerate(nums):
            while gcd(p,x)>1:
                p//=nums[l]
                l+=1
            p*=x
            b=max(b,r-l+1)
        return b