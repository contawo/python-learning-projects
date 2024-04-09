import math

a = eval(input("Enter the length of the first side: "))
b = eval(input("Enter the length of the second side: "))
c = eval(input("Enter the length of the third side: "))

s = (a + b + c) / 2
formula = s * (s - a) * (s - b) * (s - c)

def validate_number(num):
	validate = isinstance(num, int)
	if validate == True:
		return f"{num}.0"
	else: return num

if formula <= 0:
	print("Error: The input does not describe a triangle.")
else:
	area = math.sqrt(formula)
	rounded_area = float("%.2f" % (area))

	a_validated = validate_number(a)
	b_validated = validate_number(b)
	c_validated = validate_number(c)

	print(f"The area of the triangle with sides of length {a_validated} and {b_validated} and {c_validated} is {rounded_area}.")