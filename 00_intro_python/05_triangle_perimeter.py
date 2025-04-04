def main():
    # Get the side lengths of the triangle
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))
    
    all_sides: float = side1 + side2 + side3  # Calculate the perimeter

    # Print the perimeter
    print(f"The perimeter of the triangle is {all_sides}")

if __name__ == '__main__':
    main()

