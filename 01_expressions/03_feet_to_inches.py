

def main():
    inches_in_foot: int = 12  #  There are 12 inches for 1 foot.
    feet: float = float(input("Enter the number of feet: "))  # Get the number of feet.
    converted_into_inches: float = feet * inches_in_foot # Perform the conversion
    print(f"Your {feet} feet converted into inches = {converted_into_inches} inches ")
    

if __name__ == '__main__':
    main()