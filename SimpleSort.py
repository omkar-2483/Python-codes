#accept three numbers and sort them in assending order
import numpy as np
nums=np.array([0,0,0])
for i in range(3):
    nums[i]=int(input("Enter a number: "))
for i in range(2):
    if nums[i]>nums[i+1]:
        temp=nums[i]
        nums[i]=nums[i+1]
        nums[i+1]=temp
if nums[0]>nums[1]:
        temp=nums[0]
        nums[0]=nums[1]
        nums[1]=temp
print("Sorted oredr:",nums[0],nums[1],nums[2])