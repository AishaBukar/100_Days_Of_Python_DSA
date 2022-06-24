#Question 7: Two Sum


def twoSum(self, nums: List[int], target: int) -> List[int]: 
        hash_map = {}
        
        for i in range (len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [ hash_map[complement], i]
            hash_map[nums[i]] = i
        # return hash_map
        
        #Second solution
        
        # new_nums= []
        # for i in range(len(nums)-1):
        #     minValue=nums[i]
        #     minIndex= i
        #     for j in range(i+1, len(nums)):
        #         if minValue + nums[j] == target:
        #             new_nums.append(i)
        #             new_nums.append(j)
        #             return new_nums