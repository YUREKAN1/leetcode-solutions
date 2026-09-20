class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ar=[]
        for i in range(0,m):
            ar.append(nums1[i])
        for j in range(0,n):
            ar.append(nums2[j])
        ar.sort()
        nums1[:]=ar
        return nums1
        