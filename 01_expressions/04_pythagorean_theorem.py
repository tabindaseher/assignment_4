import math

def main():

# Ask the user for the lengths of the two perpendicular sides
 side_of_ab = float(input("\033[1;3mEnter the length of AB:  "))
 side_of_bc = float(input("Enter the length of BC:  "))

# Calculate the hypotenuse using the Pythagorean theorem
 hypotenuse = math.sqrt(side_of_ab ** 2 + side_of_bc ** 2)

# Output the length of the hypotenuse
 print(f"The length of the hypotenuse is: {hypotenuse}\033[0m")

 #run the program

if __name__ == '__main__':
    main() 
