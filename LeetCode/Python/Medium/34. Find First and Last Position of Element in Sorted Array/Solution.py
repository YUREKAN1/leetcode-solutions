class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
        f=0
        l=0
        for j in range(len(nums)):
            if nums[j]==target:
                f=j
                l=j
                break
        for k in range(f+1,len(nums)):
            if nums[k]==target:
                l=k
        return [f,l]