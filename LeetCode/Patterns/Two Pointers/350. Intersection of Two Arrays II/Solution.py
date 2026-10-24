class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1)>len(nums2):
            return self.intersect(nums2,nums1)
        c=Counter(nums1)
        a=[]
        for i in nums2:
            if c[i]>0:
                a.append(i)
                c[i]-=1
        return a