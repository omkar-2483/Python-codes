import numpy as np
n=int(input("Enter number of inputs:"))
nums=np.zeros(n)
for i in range(n):
    nums[i]=int(input("Enter a number: "))
sum1=np.zeros(n)
sum2=np.zeros(n)

i=0
j=n-1

for k in range(n):
    sum1[k]=nums[i]+nums[j]
    i+=1
    j-=1

k=0
i=n-1
j=0
while(k<n):
    sum2[k]=nums[i]+nums[j]
    j+=1
    i-=1
    k+=1

print('array of summation using for loop',sum1)
print('array of summation using while loop',sum2)
