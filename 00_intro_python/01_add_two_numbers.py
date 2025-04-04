def main():
    num1: str = input("Enter your first number: ")
    num1 = int(num1)  # Convert to integer
    num2: str = input("Enter your second number: ")
    num2 = int(num2)  # Convert to integer
    res: int = num1 + num2  # Add the numbers
    print(f"The total number is {res}")  # Print result

if __name__ == '__main__':
    main()  # Run the main function