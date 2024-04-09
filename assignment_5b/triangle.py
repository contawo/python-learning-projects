import math

a = eval(input("A: \n"))
b = eval(input("B: \n"))
c = eval(input("C: \n"))

s = (a + b + c) / 2
formula = s * (s - a) * (s - b) * (s - c)

def validate_number(num):
	validate = isinstance(num, int)
	if validate == True:
		return f"{num}.0"

if formula <= 0:
	print("Not a triangle")
else:
	area = math.sqrt(formula)
	rounded_area = float("%.2f" % (area))

	a_validated = validate_number(a)
	b_validated = validate_number(b)
	c_validated = validate_number(c)

	print(f"The area of the triangle with sides of length {a_validated} and {b_validated} and {c_validated} is {rounded_area}.")