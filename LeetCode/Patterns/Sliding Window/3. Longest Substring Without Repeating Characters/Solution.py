class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        maxlen=0
        seen=set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])
            currentlength=right-left+1
            maxlen=max(maxlen,currentlength)
            right+=1
        return maxlen
       