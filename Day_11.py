#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    def reverse(self, x: int) -> int:
      
        y=str(abs(x))
        
        y =y[::-1]
        
        reverse = int(y)
        
        
        if reverse <= -2 ** 31 or reverse >= 2 ** 31 -1:
            return 0
        elif x < 0:
            return - 1 * reverse
        else:
            return reverse
        
        while x !=0:
            return reverse
        
        