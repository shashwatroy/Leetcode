class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def decimalToBinary(n):  
            return bin(n).replace("0b", "") 
        l1 = list(decimalToBinary(x)) 
        l2 = list(decimalToBinary(y)) 
        print(l1,l2)
        l1.reverse()
        l2.reverse()
        print(l1,l2)
        j = 0
        if x>y :
            for i in range(len(l2)):
                if l1[i] != l2[i]:
                    j = j+1        
        else:
            for i in range(len(l1)):
                if l1[i] != l2[i]:
                    j = j+1
                    
        if len(l1)>len(l2):
            for i in range(len(l2), len(l1)):
                if l1[i] == '1':
                    j = j+1
                    
        elif len(l2)>len(l1):
            for i in range(len(l1), len(l2)):
                if l2[i] == '1':
                    j = j+1
        
        else:
            pass

        return j