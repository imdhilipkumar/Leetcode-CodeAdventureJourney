class Solution:
    def mySqrt(self, x: int) -> int:
        sq = x
        while sq * sq > x:
            sq = (sq + x // sq)//2
        return sq