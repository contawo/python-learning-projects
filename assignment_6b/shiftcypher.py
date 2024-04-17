message = input("Enter the message:\n")
key = int(input("Enter the key:\n"))

alphabets = "abcdefghijklmnopqrstuvwxyz"
cypher_message = "" # New cypher message
index = 0

while index < len(message):
	if message[index] == " ":
		# Update the cypher message with space
		cypher_message = cypher_message + " "
	else:
		position = 0 # Keep track of the position of each char in message on the alphabets
		for k in range(0, len(alphabets)):
			if message[index] == alphabets[k]:
				position = k

		cypher_position = position + key # Postion of the cypher_char

		if cypher_position >= 26:
			new_position = cypher_position - 26

			# Update the cypher message
			cypher_message = cypher_message + alphabets[new_position]
		else:
			# Update the cypher message
			cypher_message = cypher_message + alphabets[cypher_position]

	index = index + 1

print(f"Result: {cypher_message}")