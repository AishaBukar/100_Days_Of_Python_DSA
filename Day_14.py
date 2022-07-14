#Given a string s, return the longest palindromic substring in s.
def longestPalindrome(self, s: str) -> str:
        
    pal = ""
    palLen = 0
    #ababbd
    for i in range(0,len(s)):
        #odd cases
        l,r = i, i
        
        while l >= 0 and r < len(s) and s[l]==s[r]:
            if (r - l + 1) > palLen:
                pal= s[l:r+1]
                palLen = r - l + 1
            l-=1
            r+=1
        #even cases
        
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l]==s[r]:
            if (r - l + 1) > palLen:
                pal= s[l:r+1]
                palLen = r - l + 1
            l-=1
            r+=1
    return pal
        
            
    