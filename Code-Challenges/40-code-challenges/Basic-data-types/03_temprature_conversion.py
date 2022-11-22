print("Welcome to the Tempareture conversion Program")

fahrenheit = float(input("What is the given temperature in degrees Fahrenheit: "))

print(f"Degrees Fahernheit: {fahrenheit}")

# To Celsius
to_celsius = (fahrenheit - 32) * 5/9
round_to_celsius = round(to_celsius, 4)
print(f"Degrees Celsius: {round_to_celsius}")

# To Kelvin
to_kelvin = (fahrenheit - 32) * 5/9 + 273.15
round_to_kelvin = round(to_kelvin, 4)
print(f"Degrees Kelvin: {round_to_kelvin}")