class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        numbers=set(nums)
        r=[]
        for i in range(1,len(nums)+1):
            if i not in numbers:
                r.append(i)
        return r