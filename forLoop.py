#print numbersfrom 1-10 and 10-1
for i in range(1,11):
    print(i,end=",")
print()
for i in reversed(range(1,11)):
    print(i,end=",")

#input a number and find sqaure of first n natural numbers
num=int(input("Enter a number: "))
for i in range(1,num+1):
    print(i*i,end=", ")

#input a number and print its multiplication table
num =int(input("Enter a number: "))
for i in range(1,11):
    print(num*i,end=", ")

#print first 8 terms of arithmetic progression starting with 3 and having common difference of 4
start=3
for i in range(8):
    print(start,end=", ")
    start+=4

# #print first 6 terms of GP 
start=2
for i in range(6):
    print(start,end=", ")
    start*=3

#input a positive integer calculate sum of all numbers from 1 to number
num=int(input("Enter a number: "))
sum=0
for i in range(1,num+1):
    sum+=i
print("Sum of first",num,"naturals: ",sum)

#sum of receprocals of first n natural numbers
num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
    sum+=1/i
print("Sum of receprocals: ",sum)

#factorial of any positive integer
num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact*=i
print("Factorial of",num,"is: ",fact)

#WAP that inputs base and exponent and calculate value power of base to exponent 
base=int(input("Enter the base: "))
exp=int(input("Enter the exponent: "))
value=1
if(exp>=0):
    for i in range(exp):
        value*=base
else:
    exp=-exp
    for i in range(exp):
        value*=1/base
print("Value: ",value)

#input a positive number, display all factors of number and sum of all factors
num=int(input("Enter a natural number: "))
sum=0
for i in range(1,num+1):
    if num%i==0:
        print(i,end=", ")
        sum+=i
print()
print("Sum of all factors: ",sum)

#WAP that repeatedly asks user to input a positive number
# the loop will come to end when a neagtive number is enetered
#calculate sum of all enetered positve integers

sum=0
while True:
    num=int(input("Enter a positive number: "))
    if num>=0:
        sum+=num
    else:
        break
print('Sum of all enterd numbers= ',sum)