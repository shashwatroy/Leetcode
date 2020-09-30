class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l1 = s.split()
        if not l1:
            return 0
        count = 0
        for i in l1[-1]:
            count += 1
        return count
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l1 = s.split()
        if not l1:
            return 0
        else:
            return len(l1[-1])
'''
