def get_first_element(lst):
 
    print(lst[0])  # Print the first element in the list

def main():
    # Get user input for the list, one element at a time
    lst = []
    num_elements = int(input("Enter the number of elements in the list: "))
    
    for i in range(num_elements):
        element = input(f"Enter element {i+1}: ")
        lst.append(element)
    
    # Call the function to print the first element
    get_first_element(lst)

if __name__ == "__main__":
    main()


