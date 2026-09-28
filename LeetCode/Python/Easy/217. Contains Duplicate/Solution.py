class Solution(object):
    def containsDuplicate(self, nums):
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
            
        for i in d.values():
            if i>=2:
                return True
            else:
                return False        