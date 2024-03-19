import math

# Writing the formula for pi estimation
pi_formula = 2 * (2/math.sqrt(2)) * (2/math.sqrt(2 + math.sqrt(2))) * (2/math.sqrt(2 + math.sqrt(2 + math.sqrt(2))))
pi_value = round(pi_formula, 3)
print("Approximation of pi: {}".format(pi_value))

# Getting radius from user to calcuate the area
radius = eval(input("Enter the radius:\n"))

# Calculating the area using the original pi not the rounded off one
area = math.pow(radius, 2) * pi_formula
rounded_area = round(area, 3)

print(f"Area: {rounded_area}")