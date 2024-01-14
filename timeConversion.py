#accept seconds and print hr,min,sec

seconds=int(input("enter number  of seconds: "))
h=seconds//3600
sec=seconds%3600
m=sec//60
sec=sec%60
print(seconds,"sec=",h,"hrs:",m,'mins:',sec,"sec")