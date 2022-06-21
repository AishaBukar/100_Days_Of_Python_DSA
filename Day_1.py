
# Question: Checking if a string is a palindrome

def checkPalindrome(someString):
    someString = str(someString)

    reversedString = someString[::-1]

    if someString!=reversedString:
       return False
    return True

#User inputs string 
someString= input("Enter a string: ")
anyVar= checkPalindrome(someString)

#Program checks if its a palindrome
if(anyVar):
    print("It is a palindrome")
else:
    print("Not a palindrome")