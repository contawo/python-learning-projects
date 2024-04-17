string = input("Enter the full string:\n")
subsequence = input("Enter the subsequence to check for:\n")

position = 0 # Keeps track of the postion of the previous subsequence string on the full string
sub_index = 0 # Used to iterate through the loop
success = True # Validate if substring is a subsequence

while sub_index < len(subsequence):
	new_position = 0 # Keeps track of the postion of the next subsequence string on the full string

	# Checks for the position of each char of the substring in the original string
	for i in range(0, len(string)):
		if string[i] == subsequence[sub_index]:
			new_position = i

	# If the next string in the subsequence is at a position less than the previous string in the subsequence, break
	if new_position < position:
		success = False
		break
	
	position = new_position
	sub_index = sub_index + 1

# Displaying to the user
if success == True:
	print("The given substring is a subsequence of the full string.")
else:
	print("The given substring is not a subsequence of the full string.")