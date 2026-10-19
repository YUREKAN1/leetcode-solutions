class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(nums,target,k):
            l=0
            r=len(nums)-1
            i=-1

            while l<=r:
                mid=(l+r)//2
                if nums[mid]>target:
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    i=mid
                    if k:
                        r=mid-1
                    else:
                        l=mid+1
            return i
        l=binary_search(nums,target,True)
        r=binary_search(nums,target,False)
        return [l,r]