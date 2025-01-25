def print_characters_with_stars():
    user_input = input("Please type in a string: ")
    for char in user_input:
        print(char)
        print("*")

# Run the function
if __name__ == "__main__":
    print_characters_with_stars()
