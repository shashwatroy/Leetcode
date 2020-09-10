class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        l1 = list(secret)
        l2 = list(guess)
        bull = cow = 0
        seen = set()
        uniq = []

        for i in range(len(l1)):
            if l1[i] == l2[i]:
                del l1[i]
                l1.insert(0,'a')
                del l2[i]
                l2.insert(0,'b')
                bull += 1
                
        for x in l2:
            if x in l1:
                l1.remove(x)
                cow += 1
                
        return str(bull)+'A'+str(cow)+'B' 
