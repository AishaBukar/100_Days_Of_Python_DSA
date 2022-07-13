#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

def longestCommonPrefix(self, strs: List[str]) -> str:
        new_str = ""
        
        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return new_str
            new_str +=strs[0][i]
        return new_str
                  
        
        # print(strs[0][1])
        # print(strs[1])
        # print(strs[2])
            

#               j=  flower, flow, flight
             
#                  f=f
#             l=l