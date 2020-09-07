class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        L1 = str.split(" ")
        D1 = {}
        Output = []
        
        if len(L1) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in D1:
                if L1[i] not in D1.values():
                    D1[pattern[i]] = L1[i]
                else:
                    return False
                
        for i in range(len(pattern)):
            Output.append(D1[pattern[i]])
        
        if Output == L1:
            return True
        else:
            return False
