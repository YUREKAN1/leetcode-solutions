class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        c=[[] for _ in s]
        for x in range(1,len(s)):
            c[parent[x]].append(x)
        size,last=[1]*len(s),{}

        def dfs(x:int)->None:
            ch=s[x]
            above=last.get(ch,-1)
            last[ch]=x
            for child in c[x]:
                dfs(child)
            last[ch]=above
            if x:
                size[above if above>=0 else parent[x]]+=size[x]
        dfs(0)
        return size