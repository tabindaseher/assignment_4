

def main():
     # for bold and italic text
    bold_italic = '\033[1;3m'  
    reset = '\033[0m' 

    # Ask the user to be divided
    put_number = int(input(f"{bold_italic}Enter an integer number to be divided:{reset} "))
    
    # Ask the user for the divisor
    another_number = int(input(f"{bold_italic}Enter an integer number to divide by:{reset} "))
    
    # Calculate the quotient
    quotient = put_number // another_number
    
    # Calculate the remainder
    remainder = put_number % another_number
    
    # Print the result 
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# Run the program 
if __name__ == '__main__':
    main()

