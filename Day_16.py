#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

#Increment the large integer by one and return the resulting array of digits.

def plusOne(self, digits: List[int]) -> List[int]:
    digit = []

    digits= str(int(''.join([str(x) for x in digits]+1))+1)
    for x in range(len(digits)):
        digit.appendint((digits[x:x+1]))
    return digit