class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==0:    return 1
        list = [1, 1]
        for i in range(n-1):
            list[0], list[1] = list[1], list[0]+list[1]
        return list[1]
