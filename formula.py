first_number = eval(input("Enter the first number:\n"))
second_number = eval(input("Enter the second number:\n"))
third_number = eval(input("Enter the third number:\n"))

# Find the maximum value
max_number = max(first_number, second_number, third_number) 

if first_number == max_number: # Check whether the first number is the maximum
    sum = (second_number + third_number) # Sum of the second and third number
    if sum == first_number: # Check whether the sum is equal to the first number
        min_number = min(second_number, third_number) # Find the minimum between the second and third number
        max_number = max(second_number, third_number) # Find the maximum between the second and third number

        # Print the formula according to the condition - maximum + minimum = (sum of the maximum and minimum)
        print(f"The formula is: {max_number} + {min_number} = {sum}")
    else:
        print("There is no valid formula.")
elif second_number == max_number: # Check whether the second number is the maximum
    sum = (first_number + third_number) # Sum of the first and third number
    if sum == second_number: # Check whether the sum is equal to the second number
        min_number = min(first_number, third_number) # Find the minimum between the first and third number
        max_number = max(first_number, third_number) # Find the maximum between the first and third number

        # Print the formula according to the condition - maximum + minimum = (sum of the maximum and minimum)
        print(f"The formula is: {max_number} + {min_number} = {sum}")
    else:
        print("There is no valid formula.")
else:
    sum = (second_number + first_number) # Sum of the second and first number
    if sum == third_number: # Check whether the sum is equal to the third number
        min_number = min(second_number, first_number) # Find the minimum between the second and first number
        max_number = max(second_number, first_number) # Find the maximum between the second and first number

        # Print the formula according to the condition - maximum + minimum = (sum of the maximum and minimum)
        print(f"The formula is: {max_number} + {min_number} = {sum}")
    else:
        print("There is no valid formula.")
