string = input("Enter the full string:\n")
subsequence = input("Enter the subsequence to check for:\n")

success = True # Validate if substring is a subsequence

index = 0
find = 0

while index < len(subsequence):
	validate = string.lower().find(subsequence.lower()[index])

	if validate == -1:
		success = False
		break

	find = validate
	string = string[find: len(string)]
	print("Check:", string)
	index = index + 1

# Displaying to the user
if success == True:
	print("The given substring is a subsequence of the full string.")
else:
	print("The given substring is not a subsequence of the full string.")