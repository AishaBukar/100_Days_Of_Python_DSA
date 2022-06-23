#Question 6: Intersection of two arrays

#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

    i,j=0,0

#Create an empty list to store the intersected array
    arr=[]

#We need to ensure we can iterate through the entire array for the purpose of test cases

    if len(nums1)< len(nums2):
        nums1, nums2 = nums2, nums1

#Ensuring its a sorted array
        nums1, nums2 = sorted(nums1), sorted(nums2)

    while i < len(nums1) and j < len(nums2):
        
#Checking the arrays
        if nums1[i]<nums2[j]:
            i+=1
        elif nums1[i]> nums2[j]:
            j+=1
        else:
            arr.append(nums1[i])
            i+=1
            j+=1
    return arr
 