class Solution:
# Question asked what is the longest palindrome that can be **built** with 
# the given set of characters.
# find pairs from char freq
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        unpaired_chars = set()
        
        for char in s:
            if char in unpaired_chars:
                pairs += 1
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)
        
        return pairs * 2 + (1 if unpaired_chars else 0)