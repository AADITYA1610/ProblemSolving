class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        
        lenght = len(words[-1])
        return lenght
        