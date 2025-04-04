import random  

def main():
    num_sides = 6  #  sides on each die 
    
   
    dice1 = random.randint(1, num_sides)  # Roll the first die
    dice2 = random.randint(1, num_sides)  # Roll the second die

    # Calculate the total of both dice
    total = dice1 + dice2
    
    # Print the result of each die roll and the total
    print(f"Dice1 = {dice1}")
    print(f"Dice2 = {dice2}")
    print(f"The total of both dice is = {total} ")

# Run the program 
if __name__ == '__main__':
    main()


