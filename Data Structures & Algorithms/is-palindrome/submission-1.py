class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if x.isalnum()]

        l = 0 
        r = len(s)-1
        while l < r:
            if s[l] == s[r]:
                l = l+1
                r = r-1
            else: 
                return False
        return True