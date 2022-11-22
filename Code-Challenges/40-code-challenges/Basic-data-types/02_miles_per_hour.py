print("Welcome to the MPH to MPS Conversion App")

miles_per_hour = float(input("What is your speed in miles per hour: "))

# Convert to MPS
miles_per_second = miles_per_hour * 0.4474
miles_per_second = round(miles_per_second, 2)

print(f"Your speed in miles per second is {miles_per_second}")