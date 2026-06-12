class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        #res =[] 
        left_B =0
        seti = set()    # cause only set lookup is O(1)
        max_length = 0
        while l < len(s):
            if s[l] not in seti:
                seti.add(s[l])
                l+=1

            else:
                seti.clear()
                left_B +=1
                l = left_B

            max_length = max(max_length, len(seti))

        return max_length