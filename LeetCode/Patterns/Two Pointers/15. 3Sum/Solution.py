class Solution(object):
    def threeSum(self, nums):
        nums=sorted(nums)
        seen=[]
        for i in range(0,len(nums)):
            a=nums[i]
            target=0
            left=i+1
            right=len(nums)-1
            while left<right:
                if (a+nums[left]+nums[right]==0):
                    if([a,nums[left],nums[right]]) not in seen:
                        seen.append([a,nums[left],nums[right]])
                    left+=1
                elif (a+nums[left]+nums[right]>0):
                    right-=1
                else:
                    left+=1
        return seen
        