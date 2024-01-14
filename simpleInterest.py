#accept principle , rate, time and print simple intererst

p=float(input("Enter principle amount in rupees:"))
r=float(input("Enter rate of interest:"))
t=int(input("Enter number of months: "))
i=p*r*t*0.01
print("simple interest:",i)
print("simple interest: Rs.",round(i,2))