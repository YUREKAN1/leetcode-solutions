class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove=10
        a_turn=True
        while n>=remove:
            n-=remove
            remove-=1
            a_turn=not a_turn
        return not a_turn