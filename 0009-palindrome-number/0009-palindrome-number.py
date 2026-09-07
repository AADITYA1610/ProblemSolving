class Solution:
    def isPalindrome(self, x: int) -> bool:
        numb = str(x)
        rev =  numb[::-1]
        if numb == rev:
            return True
        else:
            return False