celcius = float(input("Enter the temperature in Celcius: "))
fahrenheit = (9/5) * celcius + 32
print("%0.1f degree Celcius is equal to %0.1f degree Fahrenheit " %(celcius, fahrenheit))

if (fahrenheit >= 104):
    print("It's hot!")
elif (fahrenheit <= 50):
    print("It's cold!")
else:
    print("The temperature is nice")

