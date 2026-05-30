class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            count = len(s)
            encoded += str(count)+ "#" + s 
            
        
        return encoded

    def decode(self, s: str) -> List[str]:
        listy = []
        i = 0 
        while i < len(s):
            y = s.index("#", i)

            var_len = int(s[i:y]) #includes 0 to i-1

            listy.append(s[y+1:y+1+var_len])

            i = y+1+var_len

        return listy

