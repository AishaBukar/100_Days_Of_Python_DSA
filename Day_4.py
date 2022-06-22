#Question 4: Find the first unique character in a string

def firstUniqChar(s: str) -> int:
# Create an hashmap to store the strings with unique characters for example "leetcode" would be stored as l:True, e:False,t:True etc

        hash_map = {}
        
        for i in range(0,len(s)):
            if s[i] not in hash_map:
                hash_map[s[i]] = True
            else:
                hash_map[s[i]] = False
                
        for i in range(0,len(s)):
            #If theres a unique string that sets to true, return the index i.e the first index where i=0
            if hash_map[s[i]]:
                return i