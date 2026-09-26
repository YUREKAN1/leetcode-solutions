class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        
        d=dict(knowledge)
        return re.sub(r"\((\w+)\)",lambda m:d.get(m[1],"?"),s)"""

        for x,y in knowledge:
            if x in s:
                s=s.replace("("+x+")",y)
        s=re.sub(r'\([^)]*\)','?',s)
        return s

