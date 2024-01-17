#accept a number and determine is it even or wrong
num=int(input("enter a number: "))
if(num%2==0):
    print(num,"is even number")
else:
    print(num,"is odd number")

#accept age and determine wheter he/she is eligible for voting
age=int(input("Enter your age: "))
if age>=18:
    print("you're eligible for voting")
else:
    print("you're not eligible for voting")


#accept two integers and output the largest
num1=int(input("Enter first number:"))
num2=int(input("Enter second number: "))
if num1>num2:
    print(num1,"is the largest")
elif num1==num2:
    print("numbers are equal")
else:
    print(num2,"is the largest")

#accept the number and print whether it is positive, negative or zero
num=int(input("Enter a number: "))
if num>0:
    print(num,"is positive")
elif num<0:
    print(num,"is negative")
else:
    print('number is zero')

#accept the age and print corrosponding age group
age=int(input("Enter your age: "))
if(age>=60):
    print("you belongs to 'senior citizen' group")
elif(age>=20):
    print("you belongs to 'adult' group")
elif(age>=13):
    print("you belongs to 'teenage' group")
else:
    print("you belongs to 'child' group")