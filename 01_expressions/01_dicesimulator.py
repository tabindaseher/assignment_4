import random

def main():
    # Simulate rolling two dice three times
    for i in range(3):
     # Number of sides on each die to roll
        num_sides = 6
        die1 = random.randint(1, num_sides)  # Roll the first die
        die2 = random.randint(1, num_sides)  # Roll the second die
        
        # Print the result of the dice roll
        print(f"Roll {i+1}: Your 1st Die has  = {die1} , And Your 2nd Die has = {die2}")

# Run the program
if __name__ == '__main__':
    main()


