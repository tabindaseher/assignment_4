def main():
    fav_animal: str = input("\033[1mWhat is your favorite animal?\033[0m ")  # Ask for favorite animal
    fav_animal: str = str(fav_animal)  # Ensure it's a string
    print(f"My favorite animal is {fav_animal}")  # Display the result

if __name__ == '__main__':
    main()  # Run the main function
