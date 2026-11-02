class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        def qselect(a,k):
            while True:
                if len(a)<=1:
                    return a[0]
                p=random.choice(a)
                l=[x for x in a if x<p]
                if k<len(l):
                    a=l
                    continue
                h=[x for x in a if x>p]
                if k>=len(a)-len(h):
                    k-=len(a)-len(h)
                    a=h
                    continue
                return p
        m=qselect(nums,len(nums)//2)
        return sum(abs(x-m) for x in nums)