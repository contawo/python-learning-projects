n = int(input("Enter a number between -6 and 2:\n"))

if (n < -6 or n > 2):
    print("Invalid input! The value of 'n' should be between -6 and 93.")
else:
    for value in range(n, n + 41, 7):
        if (value >= 0 and value <= 9): 
            print(" " + str(value), end="\n")
        else: 
            print(str(value), end="\n")