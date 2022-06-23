 #Question 5: Given an array, rotate the array to the right by k steps, where k is non-negative.
 
def rotate(self, nums: List[int], k: int) -> None:
    k = k % len(nums)
    nums[k:], nums[:k], =  nums[:-k], nums[-k: ]