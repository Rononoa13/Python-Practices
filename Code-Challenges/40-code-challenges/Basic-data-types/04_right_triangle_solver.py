import math

print("Welcome to the Right Triangle Solver App")

first_leg = float(input("What is the first leg of the triangle: "))
second_leg = float(input("What is the sedond leg of the triangle: "))

# Calculate hypotenuse
hypotenuse = math.sqrt(first_leg**2 + second_leg**2)
round_hypotenuse = round(hypotenuse, 3)
print(f"For a triangle with legs {first_leg} and {second_leg} the hypotenuse is {round_hypotenuse}")

# Calculate Right angled triangle
right_angled = (first_leg * second_leg) / 2
round_right_angled = round(right_angled, 3)
print(f"For a triangle with legs {first_leg} and {second_leg} the area is {round_right_angled}")
