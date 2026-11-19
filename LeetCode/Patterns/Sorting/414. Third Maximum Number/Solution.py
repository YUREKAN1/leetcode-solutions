class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        if len(set(nums))>=3:
            return sorted(set(nums))[-3]
        else:
            return sorted(set(nums))[-1]