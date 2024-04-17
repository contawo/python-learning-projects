
numbers = [321, 42, 123, 4, 534, 323, 12, 92]
set2 = [123, 5, 7, 9, 12, 85]

def oddEven(list):
	for num in list:
		if num % 2 == 0:
			return f"Even: {num}"
		else:
			return f"Odd: {num}"

def findChar(string, val):
	for i in range(0, len(string)):
		if string[i] == val:
			return i
	return -1

def string_reverse(s):
	reverse = ""
	for c in s:
		reverse = c + reverse
	return reverse

check1 = oddEven(numbers)
check2 = oddEven(set2)

# print(check1)
# print(check2)

# print(findChar("abcde", "b"))

reverse = string_reverse("ABC")
print(reverse)