first_number = eval(input("Enter the first number:\n"))
second_number = eval(input("Enter the second number:\n"))
third_number = eval(input("Enter the third number:\n"))

if (first_number + second_number) == third_number:
    minimum = min(first_number, second_number)
    maximum = max(first_number, second_number)
    sum = first_number + second_number

    print(f"The formula is: {maximum} + {minimum} = {sum}")

elif (first_number + third_number) == second_number:
    minimum = min(first_number, third_number)
    maximum = max(first_number, third_number)
    sum = first_number + third_number

    print(f"The formula is: {maximum} + {minimum} = {sum}")
    
elif (second_number + third_number) == first_number:
    minimum = min(second_number, third_number)
    maximum = max(second_number, third_number)
    sum = second_number + third_number

    print(f"The formula is: {maximum} + {minimum} = {sum}")

else:
    print("There is no valid formula.")