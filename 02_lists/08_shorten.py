MAX_LENGTH = 2  # You can adjust this value for testing

def shorten(lst):
    
    # Check if the list is longer than the MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last item from the list
        print(removed_item)  # Print the removed item

def main():
    # Example input list
    lst = ['a', 'b', 'c', 'd', 'e' ]
    
    print("Original list:", lst)
    

    shorten(lst)
    
    # Print the modified list
    print("Modified list:", lst)

if __name__ == "__main__":
    main()
