class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            while i < j and not self.isAlphaNum(s[i]):
                i += 1
            while i < j and not self.isAlphaNum(s[j]):
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True
    
    def isAlphaNum(self, c: str):
        ascii = ord(c)
        return (ord('A') <= ascii and ascii <= ord('Z') or
                ord('a') <= ascii and ascii <= ord('z') or
                ord('0') <= ascii and ascii <= ord('9'))
