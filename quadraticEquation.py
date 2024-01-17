#WAP to input coefficient of X^2, coefficient of X and Constant term and find roots of quadratic equation
import math
a=int(input("Enter the coefficient of X^2: "))
b=int(input("Enter the coefficient of X:"))
c=int(input("Enter the constant term:"))

d=(b*b)-(4*a*c)

if d<0:
    print("roots are imaginary")
elif d==0:
    root=-b/(2*a)
    print("roots are equal which are: ",round(root,2))
else:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("Roots are real and distinct, which are",round(r1,2),"and",round(r2,2))