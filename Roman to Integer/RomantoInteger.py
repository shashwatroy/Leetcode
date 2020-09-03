class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        s = list(s)
        s.reverse()
        for i in range(len(s)):
            if i>0 :
                if s[i-1]=="V" and s[i]=="I":
                    s[i-1] = 0
                    s[i] = "VI"
                elif s[i-1]=="X" and s[i]=="I":
                    s[i-1] = 0
                    s[i] = "XI"
                elif s[i-1]=="L" and s[i]=="X":
                    s[i-1] = 0
                    s[i] = "LX"
                elif s[i-1]=="C" and s[i]=="X":
                    s[i-1] = 0
                    s[i] = "CX"  
                elif s[i-1]=="D" and s[i]=="C":
                    s[i-1] = 0
                    s[i] = "DC"
                elif s[i-1]=="M" and s[i]=="C":
                    s[i-1] = 0
                    s[i] = "MC"
        
        for i in range(len(s)):
            if s[i] == "I":
                sum = sum + 1
            elif s[i] == "V":
                sum = sum + 5
            elif s[i] == "X":
                sum = sum + 10
            elif s[i] == "L":
                sum = sum + 50
            elif s[i] == "C":
                sum = sum + 100
            elif s[i] == "D":
                sum = sum + 500
            elif s[i] == "M":
                sum = sum + 1000
            elif s[i] == "VI":
                sum = sum + 4
            elif s[i] == "XI":
                sum = sum + 9
            elif s[i] == "LX":
                sum = sum + 40
            elif s[i] == "CX":
                sum = sum + 90
            elif s[i] == "DC":
                sum = sum + 400
            elif s[i] == "MC":
                sum = sum + 900
        return sum