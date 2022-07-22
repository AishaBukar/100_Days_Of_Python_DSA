# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result 
def myAtoi(self, s: str) -> int:

    max_int= 2 **31 -1
    min_int = -2 ** 31
        
    """
    :type s: str
    :rtype: bool
    """
    i=0
    negative = 1
    res= 0
    #check for white spaces
    while i < len(s) and s[i] == " ":
        i+=1
        
#check for positive value 
    if i < len(s) and s[i] == "+":
        i+=1
    
    #check for negative values
    
    elif i < len(s) and s[i] == "-":
        i+=1
        negative = -1
        
    
    #check number
    checker = set('0123456789')
    while i < len(s) and s[i] in checker:
        res = res * 10 + int(s[i])
        i+=1
    
    #check max and min
    res = res * negative
    if res < 0:   
        return (max(res, min_int))
    return (min(res, max_int))
    
    