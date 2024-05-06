# A program that does vector calculations on vectors

# Your name here
# Your Student Number here
# The Date here


import numpy as np

def magnitude(vector):
    """Calculate the magnitude of a vector."""
    return np.linalg.norm(vector)

def add_vectors(vector1, vector2):
    """Add two vectors."""
    sum = np.empty(len(vector1), dtype=float)
    
    for i in range(0, len(vector2)): # You can use either vector1 or 2, they have the same length
        sum[i] = sum[i] + vector1[i] + vector2[i]
        
    return sum

def scalar_multiply(scalar, vector):
    """Calculate the scalar multiplication of a vector."""
    scalar_multiple = np.empty(len(vector), dtype=float)
    
    for i in range(0, len(vector)):
        scalar_multiple[i] = vector[i] * scalar
    
    return scalar_multiple
    

def dot_product(vector1, vector2):
    """Calculate the dot product of two vectors."""
    product = 0
    
    for i in range(0, len(vector1)): # You can either use vector 1 or 2, they must have the same length
        product = product + (vector1[i] * vector2[i])
        
    return product

def cross_product(vector1, vector2):
    """Calculate the cross product of two vectors."""
    # Because this is static in size, I am not going to use a loop
    product = np.empty(3, dtype=float)
    
    product[0] = np.multiply(vector1[1], vector2[2]) - np.multiply(vector1[2], vector2[1])
    product[1] = np.multiply(-1, (np.multiply(vector1[0], vector2[2]) - np.multiply(vector1[2], vector2[0])))
    product[2] = np.multiply(vector1[0], vector2[1]) - np.multiply(vector1[1], vector2[0])
    
    return product
    
# Converts a given input to a vector (array)
def convert_text_to_vector(text):
    return np.array(list(map(int, text.split())))

def present_vector_as_string(vector):
    output = ""
    
    for i in range(0, len(vector)):
        if i == (len(vector) - 1):
            output = output + str(int(vector[i]))
        else:
            output = output + str(int(vector[i])) + ", "
    
    return f"({output})"

def main():
    """Main function to accept user input and call the required functions."""
    while True:
        print("\nChoose an option:")
        print("1. Magnitude of a vector")
        print("2. Vector addition")
        print("3. Scalar multiplication")
        print("4. Dot product of two vectors")
        print("5. Cross product of two 3-dimensional vectors")
        print("6. Exit")
        choice = input()
        
        if choice == "6":
            print("Exiting...")
            break
        
        elif choice == "1":
            vector_input = input("Enter space-separated components of a vector:\n")
            vector = convert_text_to_vector(vector_input)
            magnitude_answer = magnitude(vector)
            print(f"The magnitude is: {magnitude_answer}")
            
        
        elif choice == "2":
            vector1_input = input("Enter the components of the first vector separated by spaces:\n")
            vector2_input = input("Enter the components of the second vector separated by spaces:\n")
            
            vector_1 = convert_text_to_vector(vector1_input)
            vector_2 = convert_text_to_vector(vector2_input)
            
            if len(vector_1) != len(vector_2):
                print("Error: Vectors must have the same length.")
            else:
                sum = add_vectors(vector_1, vector_2)
                print(f"Sum of the vectors is: {present_vector_as_string(sum)}")
            
        
        elif choice == "3":
            vector_input = input("Enter the components of the vector separated by spaces:\n")
            scalar = eval(input("Enter the scalar:\n"))
            
            vector = convert_text_to_vector(vector_input)
            
            scalar_multiply_results = scalar_multiply(scalar, vector)
            print(f"Scalar multiple of the vectors is: {present_vector_as_string(scalar_multiply_results)}")
        
        elif choice == "4":
            vector1_input = input("Enter the components of the first vector separated by spaces:\n")
            vector2_input = input("Enter the components of the second vector separated by spaces:\n")
            
            vector_1 = convert_text_to_vector(vector1_input)
            vector_2 = convert_text_to_vector(vector2_input)
            
            dot_product_results = dot_product(vector_1, vector_2)
            print(f"Dot product of the vectors is: {dot_product_results}")
        
        elif choice == "5":
            vector1_input = input("Enter the components of the first 3-dimensional vector separated by spaces:\n")
            vector2_input = input("Enter the components of the second 3-dimensional vector separated by spaces:\n")
            
            vector_1 = convert_text_to_vector(vector1_input)
            vector_2 = convert_text_to_vector(vector2_input)
            
            cross_product_results = cross_product(vector_1, vector_2)
            print(f"Cross product of the vectors is: {present_vector_as_string(cross_product_results)}")
        
        else:
            print("Invalid choice. Please choose a valid option.")
                    
     
     
if __name__ == '__main__':
    main()
