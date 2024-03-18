print("Welcome to the Biology Expert")
print("-----------------------------")
print("Answer the following questions by selecting from among the options.")

skeleton_type = input("The skeleton is (internal/external)?\n")

if skeleton_type == "internal":
    fertilisation = input("The fertilisation of eggs occurs (within the body/outside the body)?\n")

    if fertilisation == "within the body":
        place = input("Young are produced by (waterproof eggs/live birth)?\n")

        if place == "waterproof eggs":
            covered = input("The skin is covered by (scales/feathers)?\n")

            if covered == "scales":
                print("Type of animal: Reptile")

            else:
                print("Type of animal: Bird")

        else:
            print("Type of animal: Mammal")

    else: 
        pass # Implement this section by checking on automarker on the type of questions you need to ask for this section when the user chooses "outside the body"

else:
    print("Type of animal: Arthropod")