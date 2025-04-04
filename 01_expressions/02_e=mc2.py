def main():
    # for bold and italic text
    bold_italic = '\033[1;3m'  
    reset = '\033[0m' 

    # Speed of light 
    c = 299792458
    
    # Ask the user for mass input
    mass = float(input(f"{bold_italic}Enter the mass in kilograms:{reset} "))
    
    # Calculate energy 
    energy = mass * c**2
    
    # Output the result
    print(f"The equivalent energy for {mass} kg of mass is {energy} joules.")

# Run the program
if __name__ == '__main__':
    main()
