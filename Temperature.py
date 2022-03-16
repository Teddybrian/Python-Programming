#convering temperature from celcius to farenheit or from farenheit to celcius
temperature = float(input("Enter temperature: "))
unit = input("Enter unit('C' for Celsius of 'F' for Fahrenheit): ")
if unit == 'C' or unit == 'c':
  temp1 = 9/5 * (temperature + 32)
  print("Temperature in Farenheit = ",temp1)
elif unit == 'F' or unit == 'f':
  temp2 = 5/9 * (temperature - 32)
  print("Temperature in Celcius = ",temp2)
else:
  print("Unknown unit",unit)