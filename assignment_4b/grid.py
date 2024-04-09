n = int(input("Enter a number between -6 and 2:\n"))

if (n < -6 or n > 2):
    print("Invalid input! The value of 'n' should be between -6 and 2.")
else:
    for i in range(n, n + 6): # (n + 6) - n = 6
        for k in range(n, n + 7): # (n + 7) - n = 7
            # print(f"k-value: {k}, math: {n + 7}")
            if (n >= 0 and n <= 9):
                if (k == 7):
                    print("", n, end="")
                else:
                    print("", n, end=" ")
            else:
                if (k == 7):
                    print(n, end="")
                else:
                    print(n, end=" ")
            n = n + 1
        print()