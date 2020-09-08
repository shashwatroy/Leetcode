class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            s =- 1
        else:
            s = 1
        ans = s * int(str(abs(x))[::-1])
        if -2**31 <= ans <= 2**31-1:
            return ans
        else:
            return 0
