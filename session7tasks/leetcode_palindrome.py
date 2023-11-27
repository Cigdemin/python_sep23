class Solution:
    def isPalindrome(self, x: int) -> bool:
        numb = str(x)
        palindrome = numb[::-1]
        if palindrome == numb:
            return True
        else:
            return False
        
  