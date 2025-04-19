def get_last_element(lst):
 
    print(lst[-1])  # Access the last element and print it

def main():

    lst = []
    num_elements = int(input("Enter the number of elements in the list: "))
    
    for i in range(num_elements):
        element = input(f"Enter element {i+1}: ")
        lst.append(element)
    

    get_last_element(lst)

if __name__ == "__main__":
    main()
