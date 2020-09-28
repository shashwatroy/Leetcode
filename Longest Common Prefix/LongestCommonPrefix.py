class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        x = True
        count = 0
        prefix = strs[0]
        for i in strs:
            x = True
            while(count < min(len(prefix), len(i)) and x == True):
                if prefix[count] == i[count]:
                    count += 1
                else:
                    x = False
            prefix = prefix[:count]
            count = 0
        return prefix
