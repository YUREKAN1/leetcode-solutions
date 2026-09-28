class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        r=nums[0]+nums[1]+nums[2]

        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1
            while left<right:
                t=nums[i]+nums[left]+nums[right]
                if abs(target-t)<abs(target-r):
                    r=t
                if t==target:
                    return target
                elif t<target:
                    left+=1
                else:
                    right-=1
        return r
        