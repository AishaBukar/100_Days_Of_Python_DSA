 #Question 10: Valid Palindrome
 #A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
 def isPalindrome(self, s: str) -> bool:
        
        # unwanted_chars= [":", " ", ",", ";", "!", "."]
        # s =  ''.join(i for i in s if not i in unwanted_chars).lower()
        new_s= ""
        for char in s:
            if char.isalnum():
                new_s += char.lower()
       
        
        return new_s == new_s[ :: -1]
    