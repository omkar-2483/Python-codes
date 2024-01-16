#To input numberof calls and clculate monthly bill. use given conditions

calls=int(input("Enter number of calls: "))
bill=0
if calls<=100:
    bill=200
elif calls<=150:
    bill=200+(calls-100)*0.6
elif calls<=200:
    bill=230+(calls-150)*0.5
else:
    bill=255+(calls-200)*0.4
print("bill:",bill)