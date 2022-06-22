#Question 3 : Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

def moveZeros(nums):
    #create a variable count that starts from 0
    count = 0


    for i in range (len(nums)):
        #If the number is not zero, change the index
        if nums[i] != 0:
            nums[count]= nums[i]
            count +=1

    while count < len(nums):
        nums[count] = 0
        count +=1
    return nums