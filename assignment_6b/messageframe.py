message = input("Enter the message:\n")
count = int(input("Enter the message repeat count:\n"))
thickness = int(input("Enter the frame thickness:\n"))

width = len(message) + 2 + (2 * thickness)
height = count + (2 * thickness)

# Top part above message part
for row in range(0, thickness):
	output = (row * "|") + "+" + ((width - (2 * row) - 2) * "-") + "+" + (row * "|")
	print(output)

# Middle part where there is the message
index = 0
while index < count:
	output = (thickness * "|") + f" {message} " + (thickness * "|")
	print(output)
	index = index + 1

# Bottom part below message part
for row in range(thickness - 1, -1, -1):
	output = (row * "|") + "+" + ((width - (2 * row) - 2) * "-") + "+" + (row * "|")
	print(output)