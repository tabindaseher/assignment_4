def main():

    values = []
    
    while True:
        # Ask the user to input a value
        value = input("Enter a value: ")
        

        if value == "":
            break  
        
        # Add the entered value to the list
        values.append(value)

    print("Here's the list:", values)

if __name__ == "__main__":
    main()
