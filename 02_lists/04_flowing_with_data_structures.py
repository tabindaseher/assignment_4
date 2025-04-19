def add_three_copies(data_list, data):
 
    data_list.append(data)  # Add the first copy
    data_list.append(data)  # Add the second copy
    data_list.append(data)  # Add the third copy

def main():
    # User input for data
    message = input("Enter a message to copy: ")

    # Initialize an empty list
    data_list = []

    # Print the list before modifying
    print("List before:", data_list)

   
    add_three_copies(data_list, message)

    # Print the list after modifying
    print("List after:", data_list)

if __name__ == "__main__":
    main()
