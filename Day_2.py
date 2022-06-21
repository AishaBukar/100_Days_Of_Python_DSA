#Question 2: Remove duplicates in an array

def removeDup(nums):

    i=0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i+=1
    return nums
