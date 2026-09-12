class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        a=0
        while left<right:
            h=min(height[left],height[right])
            w=right-left
            area=h*w
            
            a=max(a,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return a


        