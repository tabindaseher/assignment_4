def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))  # Get Fahrenheit input
    
    celsius = (fahrenheit - 32) * 5.0 / 9.0  # Convert to Celsius
    
    print(f"The temperature in Celsius is: {fahrenheit}F to {celsius:.2f}")  # Show result

if __name__ == '__main__':
    main()  # Run the main function
