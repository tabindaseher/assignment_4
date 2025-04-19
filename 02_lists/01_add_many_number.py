def add_many_numbers(numbers) -> int:

    total_so_far: int = 0 
    
    # Loop through each number in the list and add it to total_so_far
    for number in numbers:
        total_so_far += number
    
    return total_so_far  

def main():
    # Create a list of numbers
    numbers: list[int] = [5, 10, 15, 20]
    
    # Call the function to calculate the sum
    sum_of_numbers: int = add_many_numbers(numbers)
    
    # Print the result
    print(sum_of_numbers)  

if __name__ == '__main__':
    main()  
