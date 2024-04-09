n = int(input("Enter a number between -6 and 93:\n"))

if (n < -6 or n > 93):
    print("Invalid input! The value of 'n' should be between -6 and 93.")
else:
    for value in range(n, n + 7):
        if (value >= 0 and value <= 9): 
            print(" " + str(value), end=" ")
        else: 
            print(str(value), end=" ")