#convert temperature from celcius to farheneite

tempC=float(input("Enter temperarure in degree celcius: "))
tempF=1.8*tempC+32
print("temperature in farheneite :",tempF)

#convert temperature from farheneite to celcius
tempf=float(input("temperature in farhenheit:"))
tempc=(tempf-32)*5/9 #formula of conversion 
print('temperature in Fahrenheit is:',tempf, '°F')
print("temperature in Celsius is:",tempc, "°C")
print("round off temperature in Celsius is:",round(tempc,2),"°C")