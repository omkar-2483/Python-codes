#WAP that promts the user to enter their weight in kg and height in meter.
# the program  should calculate their body mass index
#BMI=weight/height*height
#the program then should classify  BMI into categories

weight=float(input("Enter your weight in kg:"))
height=float(input("enter your height in meter:"))
bmi=weight/(height*height)
print("Your BMI is:",round(bmi,2))

if bmi>=30:
    print("cateory: obesity")
elif bmi>=25:
    print("category: over-weight")
elif bmi>=18.5:
    print("category: normal")
else:
    print("category: under-weight")

#accept marks of three subjects from user. calculate average marks and display grades
sub1=int(input("Enter marks of subject 1: "))
sub2=int(input("Enter marks of subject 2: "))
sub3=int(input("Enter marks of subject 3: "))
avg=(sub1+sub2+sub3)/3
if avg>=90:
    print("grade: A")
elif avg>=80:
    print("grade: B")
elif avg>=70:
    print("grade: C")
elif avg>=60:
    print("grade: D")
else:
    print("grade: F")


#WAP to input a character and determine if it is a novel or consonent
char=input("Enter a character: ")
Char=char.lower();
if Char=='a' or Char=='e' or Char=='i' or Char=='o' or Char=='u':
    print(char,"is a vowel")
else:
    print(char,"is a consonent")

#WAP to determine a leap year
year=int(input("Enter a Year: "))
if year%4==0:
    if year%100==0 and year%400!=0:
        print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")