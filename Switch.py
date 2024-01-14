#accept a number 1-7 and display corrosponding day
num=int(input("Enter a number: "))
#python doesn't have in-built switch case, but you can define function for switch case

def switch(value):
    dict={
        1:"Sunday",
        2:"Monday",
        3:"Tuesday",
        4:"Wednesday",
        5:"Thursay",
        6:"friday",
        7:"Saturday"
    }
    return dict.get(value)

print("Corrosponding day: ",switch(num))