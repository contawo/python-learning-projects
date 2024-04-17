# Exercise 
# Create a loop where you ask user to enter some numbers, when the users enters a odd number you break

# while True:
# 	enter = eval(input("Enter some number: \n"))
# 	if enter % 2 != 0:
# 		break

# Task 2
# Allow the user to enter as many numbers as they want and they will enter "quit" when they are done
# Add all the even numbers that the user will enter

# add=0
# while True:
# 	enter = eval(input("Enter a number or 'quit': \n"))
# 	if enter =="quit":

# 		if enter % 2 ==0:
# 			add = add + 1
# 			print("The sum of the even numbers is",add,end=".")
# 		else:
# 			pass

# 	else:
# 		continue

sum = 0
while True:
	prompt = input("Enter a number or 'quit': \n")
	if prompt == "quit":
		break
	else:
		convert = eval(prompt)
		if convert % 2 == 0:
			sum = sum + convert

print(sum)
		
