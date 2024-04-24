# A function that detects the number of vowels in a given string
# Awonke Mnotoza

vowels = ["a", "e", "i", "o", "u"]

def is_vowel(character):
    for vowel in vowels:
        if character == vowel.lower():
            return True
    return False

def main():
    string = input("Enter a string:\n")
    count = 0
    for i in range(0, len(string)):
        if is_vowel(string[i].lower()):
            count = count + 1
    
    print(f"The number of vowels in the string is: {count}")
    
if __name__ == "__main__":
    main()