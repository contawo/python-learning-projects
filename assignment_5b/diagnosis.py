welcome_message = """--- Welcome to the Medical Diagnosis System ---
Please answer the following questions with 'yes' or 'no'"""
print(welcome_message)

has_fever = input("Do you have a fever?\n")

if has_fever == "yes":
	has_cough = input("Do you have a cough?\n")
	if has_cough == "yes":
		has_headache = input("Do you have a headache?\n")
		if has_headache == "yes":
			has_rash = input("Do you have a rash?\n")
			if has_rash == "yes":
				has_fatigue = input("Are you feeling fatigued?\n")
				if has_fatigue == "yes":
					print("Based on your symptoms, you may have one of the following conditions: influenza, malaria, typhoid")
				else:
					print("Sorry, we could not diagnose your condition based on the information provided.")
			else:
				print("Sorry, we could not diagnose your condition based on the information provided.")
		else:
			print("Sorry, we could not diagnose your condition based on the information provided.")
	else:
		print("Sorry, we could not diagnose your condition based on the information provided.")

else:
	has_cough = input("Do you have a cough?\n")
	if has_cough == "yes":
		has_headache = input("Do you have a headache?\n")
		if has_headache == "yes":
			has_rash = input("Do you have a rash?\n")
			if has_rash == "yes":
				has_fatigue = input("Are you feeling fatigued?\n")
				if has_fatigue == "yes":
					print("Based on your symptoms, you may have one of the following conditions: pneumonia, tuberculosis, bronchitis")
				else:
					print("Sorry, we could not diagnose your condition based on the information provided.")
			else:
				print("Sorry, we could not diagnose your condition based on the information provided.")
		else:
			print("Sorry, we could not diagnose your condition based on the information provided.")
	else:
		has_headache = input("Do you have a headache?\n")
		if has_headache == "yes":
			has_rash = input("Do you have a rash?\n")
			if has_rash == "yes":
				has_fatigue = input("Are you feeling fatigued?\n")
				if has_fatigue == "yes":
					print("Based on your symptoms, you may have one of the following conditions: migraine, meningitis, brain tumor")
				else:
					print("Sorry, we could not diagnose your condition based on the information provided.")
			else:
				print("Sorry, we could not diagnose your condition based on the information provided.")
		else:
			has_rash = input("Do you have a rash?\n")
			if has_rash == "yes":
				has_fatigue = input("Are you feeling fatigued?\n")
				if has_fatigue == "yes":
					print("Based on your symptoms, you may have one of the following conditions: measles, chickenpox, eczema")
				else:
					print("Sorry, we could not diagnose your condition based on the information provided.")
			else:
				has_fatigue = input("Are you feeling fatigued?\n")
				if has_fatigue == "yes":
					print("Based on your symptoms, you may have one of the following conditions: anemia, chronic fatigue syndrome, depression")
				else:
					print("Sorry, we could not diagnose your condition based on the information provided.")