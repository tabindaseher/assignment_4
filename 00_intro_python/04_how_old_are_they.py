def main():
    anton_age: int = 21  # Anton's age
    beth_age: int = anton_age + 6  # Beth is 6 years older than Anton
    chen_age: int = beth_age + 20  # Chen is 20 years older than Beth
    drew_age: int = chen_age + anton_age  # Drew's age is the sum of Chen's and Anton's ages
    ethen_age: int = chen_age  # Ethan is the same age as Chen

    # Print all friends' ages
    print(f"Anton is {anton_age} years old")
    print(f"Beth is {beth_age} years old")
    print(f"Chen is {chen_age} years old")
    print(f"Drew is {drew_age} years old")
    print(f"Ethan is {ethen_age} years old")

if __name__ == '__main__':
    main()
